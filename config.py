#!/usr/bin/env python
# encoding utf-8

USERNAME = "root"
PASSWORD = "123456"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "z1"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(
    USERNAME,
    PASSWORD,
    HOST,
    PORT,
    DATABASE
)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

