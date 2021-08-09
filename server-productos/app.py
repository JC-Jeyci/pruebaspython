from flask import Flask, jsonify
from flask.globals import request

app = Flask(__name__)

from products import products

@app.route('/ping', methods = ['GET'])
def ping():
    return jsonify({"message": "pong!"})

@app.route('/products', methods = ['GET'])
def getProducts():
    return jsonify(products)

@app.route('/products/<string:product_name>', methods = ['GET'])
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0): 
        return jsonify({"product": productsFound[0]})
    return jsonify({"message": "no se encontro el producto"})

@app.route('/products', methods = ['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }

    products.append(new_product)
    return jsonify({"message":"Product Added SuccesFully", "products":products})

@app.route('/products/<string:product_name>', methods = ['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message":"Product Update",
            "product": productFound[0]
        })
    return jsonify({"message": "no se encontro el producto"})

if __name__ == '__main__':
    app.run(debug = True, port = 4000)