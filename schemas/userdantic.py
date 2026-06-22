from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class UserRequest(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    username: str
    password: str
    model_config = ConfigDict(from_attributes=True)

class UserInfo(BaseModel):
    id: int
    username: str
    model_config = ConfigDict(from_attributes=True)

class UserToken_data(BaseModel):
    token: str
    user_info: UserInfo = Field(...,alies="userInfo") #Field() 为添加字段规则，是 Pydantic 用来给字段增加配置的函数。
    #不要使用 dict，会导致数据丢失，因为dict是可变对象，后面要创建对应的类进行替换
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
                              )

class UserMessage(UserInfo):
    """
    用户信息基础数据模型
    """
    nickname: Optional[str] = Field(None, max_length=50, description="昵称")
    avatar: Optional[str] = Field(None, max_length=255, description="头像URL")
    gender: Optional[str] = Field(None, max_length=10, description="性别")
    bio: Optional[str] = Field(None, max_length=500, description="个人简介")
