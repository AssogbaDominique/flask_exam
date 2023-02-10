from config import db
from Models.Payment import Payment


class Cash (Payment):
    id = db.Column(db.Integer, db.ForeignKey('payment.id'), primary_key=True)
    cashTendered = db.Column(db.Float, nullable = False)

    mapper_args = {
        'polymorphic_identity' : 'cash'
    }