from app import db

class Customer(db.Model):
    """Sign Up users info"""

    __tablename__="cust_info"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(30))
    email = db.Column("email", db.String, unique=True)

    def __repr__(self) -> str:
        return f'<Customer {self.email}>'