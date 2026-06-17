from select import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.usermodel import User
from schemas.userdantic import UserRequest


# 1.查找数据库中是否存在该用户
async def get_user_db(username: str, db: AsyncSession):
    stmt = select(User).where(User.useranme == username)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


# 2.注册用户到数据库
async def register_user_db(user_data: UserRequest, db: AsyncSession):
    user = User(username=user_data.username, password=user_data.password)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
