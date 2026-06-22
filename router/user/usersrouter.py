from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dependsci.db import get_db
from models.usermodel import User
from schemas.userdantic import UserRequest, UserResponse
from serverice.userservice import get_user, register_user, login_user, get_user_message
from utils.auth import get_current_user
from utils.reponse import success

router = APIRouter(prefix='/api/user', tags=['user'])


# 注册
@router.post('/register')
async def get_register(user_data:UserRequest,db: AsyncSession = Depends(get_db)):
    """
    # :param username: 用户名称
    # :param password: 用户密码
    # :由于这两个参数由用户输入，可能会存在输入格式等问题为了解决该类问题使用pydantic类型来避免
    :user_data pydantic类型
    :param db: 数据库
    :return:
    """
    # 用户注册并返回用户信息
    user_result = await register_user(user_data, db)
    # 创建一个统一的返回格式：统一前后端协议，减少人为错误，以后扩展不用改业务代码
    return success('注册成功', UserResponse.model_validate(user_result))

# 登录
@router.post('/login')
async def get_login(user_data:UserRequest,db: AsyncSession = Depends(get_db)):
    """
    登录逻辑： 先验证用户是否存在，若存在则验证密码是否正确，若正确则生成token(令牌） 返回结果，若密码不正确报错显示密码不对
    若不存在就返回用户不存在

    :param user_data:
    :param db:
    :return:
    """
    result_data = await login_user(user_data, db)
    return success('登录成功', result_data)


# 查询用户信息
@router.get('/info')
# 根据token去查用户，token不可能由用户输入，故而是有前端返回，这样就需要创建一个函数去验证token
async def get_user_info(user: User = Depends(get_current_user)):
    user_massage = await get_user_message(user)
    return success('查询成功', user_massage)