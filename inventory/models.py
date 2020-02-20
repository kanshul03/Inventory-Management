from inventory import db

class Product(db.Model):
    prod_name = db.Column(db.String(20), primary_key= True)
    prod_qty = db.Column(db.Integer, nullable = False)
    prod_price = db.Column(db.Float, nullable = False)
    def __repr__(self):
        return f"Product('{self.prod_name}','{self.prod_qty}','{self.prod_price}')"