from app import db, Users, Product

db.drop_all()
db.create_all()

testuser = Users(first_name='Mo',last_name='Darwish') # Extra: this section populates the table with an example entry
testproduct = Product(product_name='TV', price=399)
db.session.add(testuser)
db.session.add(testproduct)
db.session.commit()