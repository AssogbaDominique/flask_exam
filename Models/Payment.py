from config import db

class Payment (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    amount = db.Column(db.Float, nullable = False)
    payment_mode = db.Column(db.String(20))

    ## OneToMany de Order vers payment
    orderId = db.Column(db.Integer, db.ForeignKey('order.id'), nullable = True)
    order = db.relationship('Order', foreign_keys = [orderId])

    ## Methode pour rendre la classe Mere(Heritage)
    mapper_args = {
        'polymorphic_identity': 'payment',
        'polymorphic_on': 'payment_mode'
    }