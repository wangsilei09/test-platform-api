import time
import typing

from autotest.models.api_models import ApiCase
from autotest.schemas.api.api_report import TestReportSaveSchema
from autotest.schemas.api.timed_task import TaskKwargsIn
from autotest.services.api.api_report import ReportService
from celery_worker.worker import celery
from .test_case import async_run_testcase


@celery.task(name="zerorunner.batch_async_run_testcase")
async def batch_async_run_testcase(**kwargs: typing.Any):
    """批量执行"""
    params = TaskKwargsIn(**kwargs)
    if params.case_ids:
        kwargs['run_type'] = "case"
        for api_id in params.case_ids:
            async_run_testcase.apply_async(args=[api_id], kwargs=kwargs, __business_id=api_id)

    if params.module_ids:
        kwargs['case_env_id'] = kwargs.get("project_env_id", None)
        kwargs['run_type'] = "module"
        report_params = TestReportSaveSchema(
            name=params.name,
            run_mode=params.run_mode,
            run_type="module",
            project_id=params.project_id,
            module_id=params.module_id,
            env_id=params.project_env_id,
            exec_user_id=params.exec_user_id,
            exec_user_name=params.exec_user_name,
            start_time=time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
        )
        report_info = await ReportService.save_report_info(report_params)
        case_ids = [case_info.get("id") for case_info in await ApiCase.get_by_module_ids(params.module_ids)]
        for api_id in case_ids:
            async_run_testcase.apply_async(args=[api_id, report_info.get("id")], kwargs=kwargs, __business_id=api_id)

    if params.project_ids:
        kwargs['case_env_id'] = params.project_env_id
        kwargs['run_type'] = "project"
        report_params = TestReportSaveSchema(
            name=params.name,
            run_mode=params.run_mode,
            run_type="project",
            project_id=params.project_id,
            module_id=params.module_id,
            env_id=params.project_env_id,
            exec_user_id=params.exec_user_id,
            exec_user_name=params.exec_user_name,
            start_time=time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
        )
        report_info = await ReportService.save_report_info(report_params)
        case_ids = [case_info.get("id") for case_info in await ApiCase.get_by_project_ids(params.project_ids)]
        for api_id in case_ids:
            async_run_testcase.apply_async(args=[api_id, report_info.get("id")], kwargs=kwargs, __business_id=api_id)
