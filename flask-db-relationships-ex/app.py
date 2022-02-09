# Exercise

# Import everything we need
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__) # Declare Flask object

app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) # Declare SQLAlchemy object


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(30), nullable=False)
    orders_products = db.relationship('Orders_Products', backref='orders')
    
class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    orders_products = db.relationship('Orders_Products', backref='products')
class Orders_Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)