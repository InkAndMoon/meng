from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


def success(msg: str = "success",data=None):
    return JSONResponse(
        content=jsonable_encoder({
            "code": 200,
            "msg": msg,
            "data": data
        })
    )