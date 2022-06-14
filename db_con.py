from configparser import ConfigParser
#from models import db_user,db_admin
from app import api
from flask_sqlalchemy import SQLAlchemy


file="config.ini"
config=ConfigParser()
config.read(file)
api.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/alchemy'
#api.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+config['mysql']['user']+":"+config['mysql']['pswd']+"@"+config['mysql']['host']+"/"+config['mysql']['dbase']
#api.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#api.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/student'
db=SQLAlchemy(api)
db.init_app(api)


#class User(Base):
#__tablename__ = 'users'

'''

import configparser
import MySQLdb.cursors

config = configparser.ConfigParser()
config.read('config.ini')

def connect():
    return MySQLdb.connect(host = config['mysqlDB']['host'],
                           user = config['mysqlDB']['user'],
                           passwd = config['mysqlDB']['pass'],
                           db = config['mysqlDB']['db'])

'''