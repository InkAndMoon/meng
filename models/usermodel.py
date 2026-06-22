from datetime import datetime
from typing import Optional

from sqlalchemy import Index, Integer, String, DateTime, Enum, ForeignKey, text
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    # __table_args__ = (
    #     Index("username_UNIQUE",'username'),
    #     Index("phone_UNIQUE",'phone')
    # )   # 其实不需要，因为unique已经实现索引
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, comment="用户id")
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=True, comment="用户名")
    phone: Mapped[str] = mapped_column(String(11), unique=True,  comment="手机号")
    password: Mapped[str] = mapped_column(String(50), nullable=True, comment="密码")
    create_time: Mapped[datetime] = mapped_column(DateTime, nullable=True, comment="创建时间",
                                                  server_default=text("CURRENT_TIMESTAMP"))  # 使用数据库时间为默认值
    update_time: Mapped[datetime] = mapped_column(DateTime, nullable=True, comment="更新时间",
                                                  server_default=text("CURRENT_TIMESTAMP"),
                                                  server_onupdate=text("CURRENT_TIMESTAMP"))  # 同上
    nickname: Mapped[Optional[str]] = mapped_column(String(50), comment="昵称")
    avatar: Mapped[Optional[str]] = mapped_column(String(255), comment="头像URL",
                                                  default='https://fastly.jsdelivr.net/npm/@vant/assets/cat.jpeg')
    gender: Mapped[Optional[str]] = mapped_column(Enum('男', '女', '未知'), comment="性别",
                                                  default='未知')
    bio: Mapped[Optional[str]] = mapped_column(String(500), comment="个人简介", default='这个人很懒，什么都没留下')

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', nickname='{self.nickname}')>"


class UserToken(Base):
    """
    用户令牌表orm模型
    """
    __tablename__ = "user_token"
    # __table_args__ = (
    #     Index("token_UNIQUE", 'token'),
    #     Index("fk_user_token_user_idx", 'user_id')
    # )
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, comment="令牌id")
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False, comment="用户id")
    token: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, comment="令牌")
    expires_time: Mapped[datetime] = mapped_column(DateTime, nullable=False, comment="令牌过期时间")
    create_time: Mapped[datetime] = mapped_column(DateTime, nullable=False, comment="创建时间",
                                                  server_default=text("current_timestamp"))

    def __repr__(self):
        return f"<UserToken(id={self.id}, user_id={self.user_id}, token='{self.token}')>"
