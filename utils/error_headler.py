from starlette.responses import JSONResponse

from utils.error_oc import UserAleadyError, UserNotFoundError, PasswordError, TokenError


async def http_exception_handler(request, exc: UserAleadyError):
    """
    处理 HTTP 异常 通常是业务逻辑主动抛出的，data 保持 None
    :param request:
    :param exc:
    :return:
    当程序已经抛出 HTTPException 之后，统一把它转成 JSON 返回给前端
    """
    return JSONResponse(
        status_code=400,
        content={"code": 400, "msg": "用户已经存在", "data": None}
    )


async def user_not_found_handler(request, exc: UserNotFoundError):
    """
    处理用户不存在的异常
    :param request:
    :param exc:
    :return:
    """
    return JSONResponse(
        status_code=400,
        content={"code": 400, "msg": "用户不存在", "data": None}
    )

async def password_error_handler(request, exc: PasswordError):
    """
    处理密码错误的异常
    :param request:
    :param exc:
    :return:
    """
    return JSONResponse(
        status_code=400,
        content={"code": 400, "msg": "密码错误", "data": None}
    )

async def token_error_handler(request, exc: TokenError):
    """
    处理token不存在或过期的异常
    :param request:
    :param exc:
    :return:
    """
    return JSONResponse(
        status_code=400,
        content={"code": 400, "msg": "token不存在或过期", "data": None}
    )