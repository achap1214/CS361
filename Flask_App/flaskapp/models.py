from flaskapp import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    imageFile = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.imageFile}')"

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), nullable=False)
    mark = db.Column(db.String(10), nullable=False)
    gainLoss = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"Stock('{self.symbol}', '{self.mark}', '{self.gainLoss}')"