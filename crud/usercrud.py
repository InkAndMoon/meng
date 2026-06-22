import uuid
from datetime import datetime, timedelta

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.usermodel import User, UserToken
from schemas.userdantic import UserRequest
from utils.error_oc import TokenError


# 1.查找数据库中是否存在该用户
async def get_user_db(username: str, db: AsyncSession):
    stmt = select(User).where(User.username == username)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


# 2.注册用户到数据库
async def register_user_db(user_data: UserRequest, db: AsyncSession):
    user = User(username=user_data.username, password=user_data.password)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


# 3.令牌生成与更新
async def create_token_db(user_id: int, db: AsyncSession):
    # 生成token并设置过期时间 ——> 查询数据库里面是否有该用户的token -> 如果有则更新token，没有则创建
    # 1.生成token并设置过去时间
    token = str(uuid.uuid4())
    # timedelta(days=x,hours=y,minutes=z,seconds=t)为时间间隔类，
    expires_ar = datetime.now() + timedelta(days=7)
    # 2.查询用户是否有token
    stmt = select(UserToken).where(UserToken.user_id == user_id)
    result = await db.execute(stmt)
    user_token = result.scalar_one_or_none()
    if user_token:
        # 3.更新token
        user_token.token = token
        user_token.expires_ar = expires_ar
    else:
        # 4.创建token
        user_token = UserToken(user_id=user_id, token=token, expires_ar=expires_ar)
        db.add(user_token)
        await db.commit()
        await db.refresh(user_token)
    return user_token


# 4. 验证令牌并返回orm对象
async def get_token_user(token: str, db: AsyncSession):
    stmt = select(UserToken).where(UserToken.token == token)
    result = await db.execute(stmt)
    token_result = result.scalar_one_or_none()
    return token_result


# 4.1 根据返回的token_orm对象返回用户orm对象
async def get_token_user_info(token_result: UserToken, db: AsyncSession):
    stmt = select(User).where(User.id == token_result.user_id)
    result = await db.execute(stmt)
    user_result = result.scalar_one_or_none()
    return user_result
