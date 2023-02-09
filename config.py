from app import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# cle de hachage
app.config['SECRET_KEY']= "dom"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/order-dba"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#connexion
db = SQLAlchemy(app)

#Importations
from app import app 
from flaskext.mysql import MySQL

mysql = MySQL() ## Creer une instance mysql

####Les routes 
app.config['MYSQL_DATABASE_USER']= "root"
app.config['MYSQL_DATABASE_HOST']= "localhost"
app.config['MYSQL_DATABASE_PASSWORD']= ""
app.config['MYSQL_DATABASE_DB']= "restful-api"

#pranché
mysql.init_app(app)