from utils.error_headler import *
from utils.error_oc import *


def register_exception_handlers(app):
    """
    注册全局异常处理
    :param app:
    :return:
    """
    app.add_exception_handler(UserAleadyError, http_exception_handler)  # 注册异常处理程序，业务层报错
    app.add_exception_handler(UserNotFoundError, user_not_found_handler)
    app.add_exception_handler(PasswordError, password_error_handler)
    app.add_exception_handler(TokenError, token_error_handler)
