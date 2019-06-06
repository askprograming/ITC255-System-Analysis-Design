from Item import Item
from orderitem import OrderItem

class Order():
    def __init__(self):
        self.orderitem=[]

    def addOrderItem(self, OrderItem
        self.orderitem.append(OrderItem)

    def calcTotal(self):
        total = 0.0
        for o in self.orderitem
            total += o.getItem().price * o.quantity

        return str(total)
