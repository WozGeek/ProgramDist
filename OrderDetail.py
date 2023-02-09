from config import db

class OrderDetail(db.Model):
    id = db.Column(db.Integer,primary_key = True, nullable = False)
    creat = db.Column(db.Integer)
    shipping = db.Column(db.Integer)
    delivered = db.Column(db.Integer)
    paid = db.Column(db.Integer)
