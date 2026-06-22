from datetime import datetime

from fastapi import Header, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from crud.usercrud import get_token_user, get_token_user_info
from dependsci.db import get_db
from utils.error_oc import TokenError


# 根据前端返回的请求头中解析出token
async def get_current_user(authorization: str = Header(..., alias="Authorization"), db: AsyncSession = Depends(get_db)):
    """
    :param authorization: authorization: str=Header(...,alias = "Authorization") 有http协议规定alias = "Authorization"，就fastapi映射机制
     authorization 就是个简单变量，Header(...,alias = "Authorization")这个是有前端具体返回的请求头中带有token一行的头如Authorization: Bearer eyJhbGc...
    :param db:
    :return:
    """
    # 获取token
    token = authorization.replace("Bearer", "").strip()
    # 验证token，并返回orm对象
    token_result = await get_token_user(token, db)
    # 判断令牌是否过期或是否存在
    if not token_result or token_result.expires_ar < datetime.now():
        raise TokenError
    user_result = await get_token_user_info(token_result, db)
    return user_result
