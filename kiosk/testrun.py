from Item import Item
from orderitem import OrderItem
from order import Order

def main():

   
    item1=Item(1,'burger', 4)
    item2=Item(2,'coke', 3)
    item3 =Item(3,'chicken nuggets', 4)

    OrderItem1=OrderItem(item1,2)
    OrderItem2=OrderItem(item2,1)
    OrderItem3=OrderItem(item3,5)

    Order = Order()
    order.addOrderItems(OrderItem1)
    order.addOrderItems(OrderItem2)
    order.addOrderItems(OrderItem3)

    totalCost = Order.calculateTotal()
    print("Total is: $" + totalCost)

    main()

    