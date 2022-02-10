from application import db

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(20))
    