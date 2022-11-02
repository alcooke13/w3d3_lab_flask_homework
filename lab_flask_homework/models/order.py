from datetime import datetime

class Order():

    def __init__(self, customer_name, quantity, pizza_name, extra_toppings):
        now = datetime.now()
        
        self.customer_name = customer_name
        self.quantity = quantity
        self.pizza_name = pizza_name
        self.order_date = now.strftime("%H: %M: %S")
        self.extra_toppings = extra_toppings
        
        
