from fastapi import APIRouter

from autotest.schemas.api.story import StoryQuery, StoryIn, StoryId
from autotest.services.api.story import StoryService
from autotest.utils.response.http_response import partner_success

router = APIRouter()


@router.post('/list', description="功能列表")
async def module_list(params: StoryQuery):
    data = await StoryService.list(params)
    return partner_success(data)


@router.post('/getAllModule', description="获取所有功能")
async def get_all_module():
    data = await StoryService.get_all()
    return partner_success(data)


@router.post('/saveOrUpdate', description="更新保存功能")
async def save_or_update(params: StoryIn):
    data = await StoryService.save_or_update(params)
    return partner_success(data)


@router.post('/deleted', description="删除功能")
async def deleted(params: StoryId):
    data = await StoryService.deleted(params)
    return partner_success(data)
