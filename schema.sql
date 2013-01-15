drop table if exists users;
create table users (
    id integer primary key autoincrement,
    email varchar(100) not null unique,
    password varchar(100) not null,
    first_name varchar(100) not null,
    last_name varchar(100) not null,
    username varchar(100) not null unique,
    date_signed_up date not null,
    date_last_login date,
    date_last_activity date,
    password_reset_code varchar(200)
);

create table useremails (
    id integer primary key autoincrement,
    user_id integer not null,
    email varchar(100) not null,
    date_added date,
    verification not null
);

create table userapps (
    id integer primary key autoincrement,
    user_id integer not null,
    app_id integer not null,
    status integer
);

create table apps (
    id integer primary key autoincrement,
    app_name varchar(100) not null
);

