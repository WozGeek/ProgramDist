from config import db
import enum
from sqlalchemy import Enum

class Customer(db.Model):
    id = db.Column(db.Integer,primary_key = True, nullable = False)
    name = db.Column(db.String(155))
    deliveryAddress = db.Column(db.String(155), nullable = False)
    contact = db.Column(db.String(155), nullable = False)
    active = db.Column(db.Boolean, nullable = False)

class Item(db.Model):
    id = db.Column(db.Integer,primary_key = True, nullable = False)
    weight = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(155), nullable = False)

class Order(db.Model):
    id = db.Column(db.Integer,primary_key = True, nullable = False)
    createDate = db.Column(db.Date, nullable=False)

class OrderDetail(db.Model):
    id = db.Column(db.Integer,primary_key = True, nullable = False)
    creat = db.Column(db.Integer)
    shipping = db.Column(db.Integer)
    delivered = db.Column(db.Integer)
    paid = db.Column(db.Integer)

class OrderStatus(enum.Enum):
    CREATE = 0
    SHIPPING = 1
    DELIVERED = 2
    PAID = 3
'''
t= Table(
    'data', MetaData(), Column('value', Enum(OrderStatus))
)

connection.execute(t.insert(), {"value": OrderStatus.SHIPPING})
assert connection.scalar(t.select()) is OrderStatus.SHIPPING
'''
class Payement(db.Model):
    id = db.Column(db.Integer,primary_key = True, nullable = False)
    amount = db.Column(db.Float, nullable=False)
    paymentMode = db.Column(db.String(121), nullable = False)
    __mapper_args__ = {'polymorphic_on':paymentMode}

class Credit(Payement):
    id=db.Column(db.Integer,primary_key=True, nullable=False)
    number = db.Column(db.Float, nullable = False)
    type = db.Column(db.String(121), nullable = False)
    expireDate = db.Column(db.Date, nullable = False)
    __mapper_args__ = {'polymorphic_identity': "Credit" }

class Cash(Payement):
    id=db.Column(db.Integer,primary_key=True, nullable=False)
    cashTendered = db.Column(db.Float, nullable=False)
    __mapper_args__ = {'polymorphic_identity': "Cash"}

class Check(Payement):
    id=db.Column(db.Integer,primary_key=True, nullable=False)
    name = db.Column(db.String(121), nullable = False)
    bankID = db.Column(db.String(121), nullable=False)
    __mapper_args__ = {'polymorphic_identity': "Check"}
    

class WireTransfert(Payement):
    id=db.Column(db.Integer,primary_key=True, nullable=False)
    bank = db.Column(db.String(121), nullable=False)
    bankName = db.Column(db.String(121), nullable=False)
    __mapper_args__ = {'polymorphic_identity':"WireTransfert"}

