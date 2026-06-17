from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from crud.usercrud import get_user_db, register_user_db
from dependsci.db import get_db
from schemas.userdantic import UserRequest


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
    return await register_user_db(user_data, db)