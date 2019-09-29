import unittest
import sys
sys.path.append('..')
import shopping_cart

class ShoppingCartTestCases(unittest.TestCase):
  def setUp(self):
    self.cart = shopping_cart.ShoppingCart()

  def test_cart_property_initialization(self):
    self.assertEqual(self.cart.subtotal, 0, msg='Initial value of subtotal not correct')
    self.assertIsInstance(self.cart.items, dict, msg='Items is not a dictionary')

  def test_add_item(self):
    self.cart.add_item('Sardines', 3)
    self.assertEqual(self.cart.add_item('Baked Beans', 3), 'Added Baked Beans to basket')
    self.assertNotEqual(self.cart.add_item('xcfgb', 3), 'Added Baked Beans to basket')

    self.assertAlmostEqual(self.cart.subtotal, 8.64, msg='Cart subtotal not correct after adding items')
    self.assertEqual(self.cart.items['Sardines'], 3, msg='Quantity of items not correct after adding item')

  def test_remove_item(self):
    self.cart.add_item('Biscuits', 3)
    self.cart.remove_item('Biscuits', 2)

    self.assertAlmostEqual(self.cart.subtotal, 1.20, msg='Cart subtotal not correct after removing item')
    self.assertEqual(self.cart.items['Biscuits'], 1, msg='Quantity of items not correct after removing item')

  def test_checkout_case1(self):
    self.cart.add_item('Baked Beans', 4)
    self.cart.add_item('Biscuits', 1)

    self.cart.checkout()
    self.assertAlmostEqual(self.cart.subtotal, 5.16, msg='Incorrect amount for subtotal')
    self.assertAlmostEqual(self.cart.discount, 0.99, msg='Incorrect amount for discount')
    self.assertAlmostEqual(self.cart.total, 4.17, msg='Incorrect amount for total')

  def test_checkout_case2(self):
    self.cart.add_item('Baked Beans', 2)
    self.cart.add_item('Biscuits', 1)
    self.cart.add_item('Sardines', 2)

    self.cart.checkout()
    self.assertAlmostEqual(self.cart.subtotal, 6.96, msg='Incorrect amount for subtotal')
    self.assertAlmostEqual(self.cart.discount, 0.95, msg='Incorrect amount for discount')
    self.assertAlmostEqual(self.cart.total, 6.01, msg='Incorrect amount for total')
    

if __name__ == '__main__':
    unittest.main()