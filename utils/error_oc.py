from fastapi import HTTPException, Request
from starlette.responses import JSONResponse


# 只是用来抛出异常状态的。是一个类 切记
class UserAleadyError(Exception):
    """
    用户已经存在的error
    :return:
    """
    pass


class  UserNotFoundError(Exception):
    """
    用户不存在的error
    :return:
    """
    pass


class PasswordError(Exception):
    """
    密码错误
    :return:
    """
    pass


class TokenError(Exception):
    """
    token不存在或过期
    :return:
    """
    pass
