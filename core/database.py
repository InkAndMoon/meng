"""
    数据库绑定： 创建引擎，创建会话工厂
"""
# 1. 导包
from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine,async_sessionmaker

# 2. 创建引擎
sql_url = "mysql+asyncio://root:2004616@localhost/news_app?charset=utf8mb4"
engine = create_async_engine(
    sql_url,
    echo=True,  # 打印日志
    pool_size=10,   # 连接池大小
    pool_recycle=3600,  # 连接回收时间
    max_pool_overflow=20,  # 连接池溢出时，最多允许的连接数
)

# 3. 创建会话工厂
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,  # 提交时，不关闭连接
)