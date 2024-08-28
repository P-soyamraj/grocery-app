from flask import Flask,request,jsonify
from product_dao import get_all_products
app = Flask(__name__)

@app.route('/getProducts', methods=['GET'])
def get_products():
    products = get_all_products()
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
if __name__ == "__main__":
    print("Starting Python Flask Server for Grocery store Management System ")
    app.run(port=8000)