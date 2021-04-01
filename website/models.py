from website import db

class phone(db.Model):
    phone_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)

