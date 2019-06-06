import unittest
from item import Item
import orderitem import Orderitem
from order import Order

class ItemTest(unittest.TestCase):
    def setUp(self):
        self.Item=Item(1,'item1',4.00)
    def test_string(self):
        self.assertEqual(srt(str.item), self.item.itemname )
    def test_GetItemNumber(self):
        self.assertEqual(self.item.getItemNumber(),1)
    def test_GetItemPrice(self):
        self.assertEqual(self.item.getItemPrice(),4.00)
class OrderItem(unittest.TestCase):
    def setUp(self):
        self.item=Item(1,'item',4.00)
        self.oitem=OrderItem(self.item, 2)

    def test_Quantity(self):
        self.assertEqual(self.oitem.getQuantity(),2)
    def test_item(self):
        item=self.oitem.getItem()
        self.assertEqual(str(item),'item1')
class OrderTest(unittest.TestCase):
    def setUp(self):
        self.item1=Item(1, 'burger', 6.25)
        self.item2=Item(2, 'coke', 4.50)
        self.item3=Item(3, 'chicken nuggets', 4.50)

        self.orderitem1=OrderItem(self.item1,1)
        self.orderitem2=OrderItem(self.item2,3)
        self.orderitem3=OrderItem(self.item3,2)

        self.order=order():
        self.order.addOrderItems(self.orderitem1)
        self.order.addOrderItems(self.orderitem2)
        self.order.addOrderItems(self.orderitem3)

    def test_CalculateTotal(self):
        payment=self.order.test_CalcTotal()
        self.assertEqual(str(total))