from flask import render_template
from app import app
from models.order_list import *


@app.route('/orders')
def index():
    return render_template('order.html', title='order', list_of_orders = list_of_orders)

@app.route('/orders/<index>')
def single_order(index):
    chosen_order = list_of_orders[int(index)]
    return render_template('order_1.html', title='order', order=chosen_order)

# @app.route('/orders/2')
# def order_2():
#     return render_template('order_1.html', title='order', order=list_of_orders[1])

# @app.route('/orders/3')
# def order_3():
#     return render_template('order_1.html', title='order', order=list_of_orders[2])