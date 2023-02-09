from config import db
from Payement import Payement

class Cash(Payement):
    id=db.Column(db.Integer,primary_key=True, nullable=False)
    cashTendered = db.Column(db.float, nullable=False)
    __mapper_args__ = {'polymorphic_identity': "Cash"}
    