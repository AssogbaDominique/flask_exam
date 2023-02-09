from config import db
import enum
from sqlalchemy import Enum

class Customer(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    name=db.Column(db.String(120), nullable=False)
    deliveryAddress=db.Column(db.String(120), nullable=False)
    contact=db.Column(db.String(120), nullable=False)
    active=db.Column(db.Boolean, nullable=False)

class Item(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    name=db.Column(db.String(120), nullable=False)
    description=db.Column(db.Float, nullable=False)

class Order(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    createDate=db.Column(db.Date, nullable=False)

class OrderDetail(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    qty=db.Column(db.Integer, nullable=False)
    taxStatus=db.Column(db.String(120), nullable=False)

class OrderStatus(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    CREATE = db.Column(db.Integer, nullable=False)
    SHIPPING = db.Column(db.Integer, nullable=False)
    DELIVERED = db.Column(db.Integer, nullable=False)
    PAID = db.Column(db.Integer, nullable=False)

#class Payment(db.Model):
  #  id = db.Column(db.Integer, primary_key=True, nullable=False)