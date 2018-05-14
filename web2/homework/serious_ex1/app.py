from flask import Flask, render_template
from models.collection import Customer
import mlab
from jinja2 import Template
app = Flask(__name__)

mlab.connect()

@app.route('/customer')
def index():
    return render_template('index.html')

@app.route('/customer,<g>')
def customer(g):
    #customer ở dạng list
    customer_list = []
    customer = Customer.objects(gender = g, contacted = False) # collection object trỏ vào dictionary tìm dictionary vs key gender =0
    for index, item in enumerate(customer):
        if index < 10:
            customer_list.append(item)
    return render_template("customer.html",customer = customer_list)

if __name__ == '__main__':
  app.run( debug=True)
