show databases;

use fast;

create table user(
    id int primary key auto_increment,
    username varchar(20) not null,
    password varchar(20) not null
);

show tables;

drop table if exists user;

create table if not exists users(
    id int primary key auto_increment ,
    username varchar(50) unique not null,
    phone varchar(11) unique,
    password varchar(50) not null,
    create_time timestamp default current_timestamp ,
    update_time timestamp default current_timestamp on update current_timestamp,
    nickname varchar(50),
    avatar varchar(255) ,
    gender Enum('男', '女', '未知') default '未知',
    # enum 枚举类型
    bio varchar(255)
);
# 这两个字段已经 unique了 mysql会自动创建索引。
# create index username_UNIQUE on users(username);
# create index phone_UNIQUE on users(phone);
select * from users;


create table if not exists user_token(
    id int primary key auto_increment,
    user_id int not null,
    token varchar(255) not null unique ,
    expires_time timestamp not null,
    create_time timestamp default current_timestamp ,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

select * from user_token;



alter table users modify phone varchar(11) null;
