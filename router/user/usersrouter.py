from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dependsci.db import get_db
from schemas.userdantic import UserRequest
from serverice.userservice import get_user, register_user

router = APIRouter(prefix='/api/user', tags=['user'])

# 注册
@router.get('/register')
async def get_register(user_data:UserRequest,db: AsyncSession = Depends(get_db)):
    """
    # :param username: 用户名称
    # :param password: 用户密码
    # :由于这两个参数由用户输入，可能会存在输入格式等问题为了解决该类问题使用pydantic类型来避免
    :user_data pydantic类型
    :param db: 数据库
    :return:
    """
    # 1. 查询用户是否存在
    user = await get_user(user_data.username, db)
    if user:
        return {'code': 1, 'msg': '用户已存在'}
    user_result = await register_user(user_data, db)
    return {
        'code': 0,
        'msg': '注册成功',
        'data': {
            'username': user_result.username,
            'password': user_result.password
        }
            }