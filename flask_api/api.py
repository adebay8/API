from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


PRODUCTS = {
    "0":{'name': 'Gucci Bag','price': '$5000',"in-stock":"yes"},
    '1':{'name': 'iPhone X', 'price': '$1000',"in-stock":"yes"},
    '2':{'name': 'Notebook','price': '$10',"in-stock":"yes"}
}

parser = reqparse.RequestParser()

class ProductsList(Resource):
  def get(self):
      return PRODUCTS
  def post(self):
      parser.add_argument("name")
      parser.add_argument("price")
      parser.add_argument("in-stock")
      args = parser.parse_args()
      product_id = int(max(PRODUCTS.keys())) + 1
      product_id = '%i' % product_id
      PRODUCTS[product_id] = {
        "name": args["name"],
        "price": args["price"],
        "in-stock": args["in-stock"],
      }
      return PRODUCTS[product_id], 201

api.add_resource(ProductsList, '/products/')

class Product(Resource):
  def get(self, product_id):
      if product_id not in PRODUCTS:
          return "Not found", 404
      else:
          return PRODUCTS[product_id]

  def put(self, product_id):
      parser.add_argument("name")
      parser.add_argument("price")
      parser.add_argument("in-stock")
      args = parser.parse_args()
      if product_id not in PRODUCTS:
        return "Record not found", 404
      else:
        product = PRODUCTS[product_id]
        product["name"] = args["name"] if args["name"] is not None else product["name"]
        product["price"] = args["pricee"] if args["price"] is not None else product["price"]
        product["in-stock"] = args["in-stock"] if args["in-stock"] is not None else product["in-stock"]
      return product, 200

  def delete(self, product_id):
      if product_id not in PRODUCTS:
        return "Not found", 404
      else:
        del PRODUCTS[product_id]
        return '', 204

api.add_resource(Product, '/products/<product_id>')


if __name__ == "__main__":
  app.run(debug=True)