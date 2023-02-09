from config import db
from Payement import Payement

class WireTransfert(Payement):
    id=db.Column(db.Integer,primary_key=True, nullable=False)
    bank = db.Column(db.String(121), nullable=False)
    bankName = db.Column(db.String(121), nullable=False)
    __mapper_args__ = {'polymorphic_identity':"WireTransfert"}

