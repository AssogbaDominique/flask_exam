from config import db
from Models.Payment import Payment

class Cash (Payment):
    id = db.Column(db.Integer, db.Foreign_Key('payment.id'), primary_key=True)
    cashTendered = db.Column(db.Float, nullable = False)

    _mapper_args_ = {'polymorphic_identity' : 'cash'}
