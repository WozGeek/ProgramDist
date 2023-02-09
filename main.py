from app import app 
from config import db
from models import Payement, Customer, Order, OrderDetail, OrderStatus, Item
from flask import request, jsonify

app.app_context().push()
db.drop_all()
db.create_all()

@app.route('/animal/add', methods=['POST'])
def add_customer():
    try:
        json = request.json
        name = json["name"]
        deliveryAddress = json['deliveryAddress']
        contact = json["contact"]
        active = json['active']
        if name and deliveryAddress and contact and request.method == 'POST':
            customer = Customer(name = name, deliveryAddress = deliveryAddress, contact = contact, active = active)
            db.session.add(customer)
            db.session.commit()
            resulat = jsonify('Customer a été bien enregister')
            return resulat
    except Exception as e:
        print(e)
        resulat = {"message":"Nous avons rencontré un problème"}
        return jsonify(resulat)