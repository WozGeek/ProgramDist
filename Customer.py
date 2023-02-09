from config import db

class Custumer(db.Model):
    id = db.Column(db.Integer,primary_key = True, nullable = False)
    name = db.Column(db.String(155))
    deliveryAddress = db.Column(db.String(155), nullable = False)
    contact = db.Column(db.String(155), nullable = False)
    active = db.Column(db.boolean, nullable = False)