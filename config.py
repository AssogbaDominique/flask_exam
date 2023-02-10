from app import app
from flask_sqlalchemy import SQLAlchemy


# cle de hachage
app.config['SECRET_KEY']= "dom"

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/order-dba"

#connexion
db = SQLAlchemy(app)

