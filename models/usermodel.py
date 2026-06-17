from datetime import datetime
from typing import Optional

from sqlalchemy import Index, Integer, String, DateTime, Enum
from sqlalchemy.orm import mapped_column,Mapped,DeclarativeBase


class Base(DeclarativeBase):
    pass

class User(Base):
        __tablename__ = "users"
        __table_args__ = (
            Index("username_UNIQUE",'username'),
            Index("phone_UNIQUE",'phone')
        )
        id: Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True,comment="用户id")
        useranme: Mapped[str] = mapped_column(String(50),unique=True,nullable=True,comment="用户名")
        phone: Mapped[str] = mapped_column(String(11),unique=True,nullable=True,comment="手机号")
        password: Mapped[str] = mapped_column(String(50),nullable=True,comment="密码")
        create_time: Mapped[datetime] = mapped_column(DateTime,nullable=True,comment="创建时间",default=datetime.now())
        update_time: Mapped[datetime] = mapped_column(DateTime,nullable=True,comment="更新时间",default=datetime.now())
        nickname: Mapped[Optional[str]] = mapped_column(String(50), comment="昵称")
        avatar: Mapped[Optional[str]] = mapped_column(String(255), comment="头像URL",
                                                      default='https://fastly.jsdelivr.net/npm/@vant/assets/cat.jpeg')
        gender: Mapped[Optional[str]] = mapped_column(Enum('male', 'female', 'unknown'), comment="性别",
                                                      default='unknown')
        bio: Mapped[Optional[str]] = mapped_column(String(500), comment="个人简介", default='这个人很懒，什么都没留下')
        def __repr__(self):
            return f"<User(id={self.id}, username='{self.username}', nickname='{self.nickname}')>"