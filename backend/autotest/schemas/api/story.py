from pydantic import Field, BaseModel

from autotest.schemas.base import BaseSchema


class StoryIn(BaseModel):
    id: int = Field(None, description="id")
    name: str = Field(..., description="项目名称")
    project_id: int = Field(..., description="项目名称")
    module_id: str = Field(..., description="模块id")
    jira_task: str = Field(None, description="jira任务")
    dev_user: str = Field(None, description="开发人员")
    test_user: str = Field(None, description="测试人员")
    story_url: str = Field(None, description="story链接")
    remarks: str = Field(None, description="其他信息'")


class StoryQuery(BaseSchema):
    """查询参数序列化"""

    id: int = Field(None, description="id")
    name: str = Field(None, description="项目名称")
    project_name: str = Field(None, description="项目名称")
    project_id: int = Field(None, description="项目id")
    module_id: int = Field(None, description="模块id")
    order_field: str = Field(None, description="排序字段")
    sort_type: str = Field(None, description="排序类型")
    created_by_name: str = Field(None, description="创建人名称")


class StoryId(BaseSchema):
    id: int = Field(..., description="id")
