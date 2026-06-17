import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from router.user import usersrouter

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    # 允许访问的源（网络地址）
    allow_credentials=False,    # 允许携带cookie
    allow_methods=["*"],    # 允许的请求方法
    allow_headers=["*"],    # 允许的请求头
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


#挂载路由
# 现在只挂载用户
app.include_router(usersrouter.router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000,reload= True)
