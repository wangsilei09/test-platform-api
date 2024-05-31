import typing

from autotest.exceptions.exceptions import ParameterError
from autotest.models.api_models import StoryInfo, ApiCase
from autotest.schemas.api.story import StoryQuery, StoryIn, StoryId
from autotest.utils.response.codes import CodeEnum


class StoryService:
    """功能"""

    @staticmethod
    async def list(params: StoryQuery) -> typing.Dict:
        """
        获取模块列表
        :param params: 查询参数
        :return:
        """
        data = await StoryInfo.get_list(params)
        return data

    @staticmethod
    async def get_all() -> typing.Dict:
        """
        获取模块列表
        :return:
        """
        data = await StoryInfo.get_all()
        return data

    @staticmethod
    async def save_or_update(params: StoryIn) -> typing.Dict:
        """
        模块保存方法
        :param params: 参数
        :return:
        """
        # 当模块关联的包发生变更时，原始包移除模块信息
        same_name_module = await StoryInfo.get_module_by_name(params.name)
        if params.id:
            module_info = await StoryInfo.get(params.id)
            if module_info.name != params.name:
                if await StoryInfo.get_module_by_name(params.name):
                    raise ParameterError(CodeEnum.MODULE_NAME_EXIST)
        else:
            if same_name_module:
                raise ParameterError(CodeEnum.MODULE_NAME_EXIST)
        return await StoryInfo.create_or_update(params.dict())

    @staticmethod
    async def deleted(params: StoryId):
        """
        删除模块
        :param params:
        :return:
        """
        if params.id:
            relation_api = await ApiCase.get_api_by_story_id(params.id)
            if relation_api:
                raise ParameterError(CodeEnum.MODULE_HAS_CASE_ASSOCIATION)
            return await StoryInfo.delete(params.id)
