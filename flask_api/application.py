
from flask import Flask, render_template, abort
from flask import jsonify
from flask import request
app = Flask(__name__)
products=[
 {
 "id":"1",'name': 'Gucci Bag','price': '$5000',"in-stock":"yes"},
 {
 "id":"2",'name': 'iPhone X', 'price': '$1000',"in-stock":"yes",}
 ]

@app.route('/', methods=['GET'])
def home(): 
    return render_template("index.html")

@app.route('/products/product',methods=['GET'])
def getAllprod():
    return jsonify({'products':products})

@app.route('/products/product/<productID>',methods=['GET'])
def getprod(productID):
    usr = [ prod for prod in products if (prod['id'] == productID) ] 
    return jsonify({'prod':usr})

@app.route('/products/product/<productID>',methods=['PUT'])
def updateprod(productID):
    em = [ prod for prod in products if (prod['id'] == productID) ]
    if 'name' in request.json : 
        em[0]['name'] = request.json['name']
    if 'in-stock' in request.json:
        em[0]['in-stock'] = request.json['in-stock']
    return jsonify({'prod':em[0]})

@app.route('/products/product',methods=['POST'])
def createprod():
    dat = {
    'id':request.json['id'],
    'name':request.json['name'],
    'price':request.json['price'],
    'in-stock':request.json['in-stock']}
    products.append(dat)
    return jsonify(dat)

@app.route('/products/product/<productID>',methods=['DELETE'])
def deleteprod(productID):
    em = [ prod for prod in products if (prod['id'] == productID) ]
    if len(em) == 0:
       abort(404)
    products.remove(em[0])
    return jsonify({'response':'Success'})
if __name__ == '__main__':
 app.run()