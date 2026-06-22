from fastapi import Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from crud.usercrud import get_user_db, register_user_db, create_token_db
from dependsci.db import get_db
from models.usermodel import User
from schemas.userdantic import UserRequest, UserInfo, UserToken_data, UserMessage
from utils.error_headler import user_not_found_handler
from utils.error_oc import *


# 1.查询用户是否在数据库
async def get_user(username, db: AsyncSession):
    """
    :param username: 用户名称
    :param db: 数据库
    :return:
    """
    result = await get_user_db(username, db)
    return result


# 2.用户注册
async def register_user(user_data: UserRequest, db: AsyncSession):
    """
    :param user_data: 用户数据,pydantic类型
    :param db: 数据库
    :return:
    """
    user_result = await get_user(user_data.username, db)
    if user_result:
        raise UserAleadyError()
        # service高度依赖fastapi,出现高耦合的情况，需考虑解耦。可写全局处理器，service只抛出错误码，全局处理器处理错误码并返回错误信息
    return await register_user_db(user_data, db)


# 3.用户登录
async def login_user(user_data: UserRequest, db: AsyncSession):
    """
    1.验证用户是否存在
    2.验证密码是否正确
    3.生成token
    4.响应结果
    :param user_data:
    :param db:
    :return:
    """
    user_result = await get_user(user_data.username, db)
    if not user_result:
        raise UserNotFoundError()
    if user_result.password != user_data.password:
        raise PasswordError()
    token = await create_token_db(user_result.id, db)
    result_data = UserToken_data(token=token.token, user_info=UserInfo.model_validate(user_result))
    return result_data


# 4.查询用户信息
async def get_user_message(user: User):
    result_data = UserMessage.model_validate(user)
    return result_data
