from config import db

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    amount = db.Column(db.Float, nullable  = False)
    
    ##### Liaison 
    #### OneToMany
    orderId = db.Column(db.Integer, db.Foreign_Key('order.id'), nullable = True)
    order = db.relationship('Order', foreign_keys = [orderId])
        ## Methode pour rendre la classe Mere(Heritage)
    
    _mapper_args_ = {
        'polymorphic_identity': 'payment',
        'polymorphic_on': 'payment_mode'
    }
