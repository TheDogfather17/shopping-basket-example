from config import *
class ShoppingCart(object):

    def __init__(self):
      self.subtotal = 0
      self.discount = 0
      self.total = 0
      self.items = {}
      
    def add_item(self, item_name, quantity):
        if item_name not in catalogue:
          return ('Choose one of the products available: \n', catalogue)
        else:
          price = catalogue[item_name]
          self.subtotal += (quantity * price)
          if item_name in self.items:
            self.items[item_name] += quantity
          else:
            self.items[item_name] = quantity
          return 'Added ' + item_name + ' to basket'

    def remove_item(self, item_name, quantity):
      price = catalogue[item_name]
      self.subtotal -= (quantity * price)
      if quantity > self.items[item_name]:
        del self.items[item_name]
      self.items[item_name] -= quantity

    def clear_basket(self):
      self.subtotal = 0
      self.discount = 0
      self.total = 0
      self.items = {}
      
    def checkout(self):
      if self.subtotal > 0: 
        self.discount = (discount(self.items, catalogue))
        self.total = self.subtotal - self.discount
        self.subtotal = round(self.subtotal + 0.0000001, 2)
        self.discount = round(self.discount + 0.0000001, 2)
        self.total = round(self.total, 2)
        return 'Subtotal:', self.subtotal, 'Discount:', self.discount, 'Total:', self.total

