## Documentation

This shopping cart test is designed with a static basket with only a few items labelled as Catalogue. 

There are no dependencies outside the python standard library. 

Run the unit tests through the test file or import the shopping_cart file into your own python session to start using the basket and its methods. 

Run the unit tests through cmd/powershell/terminal: 
python .\test_basket.py

# Shopping Cart

## Catalogue 

### catalogue = 
* {
* 'Baked Beans' : 0.99,
*  'Biscuits' : 1.20,
*  'Sardines' : 1.89,
* 'Shampoo (Small)' : 2.00,
*  'Shampoo (Medium)' : 2.50,
*  'Shampoo (Large)' : 3.50
*  }

### Adding Items 

The add item function adds an item from the catalogue to the basket. This is a very simple fucntion and the spelling of the items from the catalog needs to be as specified above. It takes 2 argumentss, the name of the item and a quantity. 

> add_item('Baked Beans', 2)

this will add 2 items, Baked Beans into the basket at the price displayed in the catalog

### Removing Items 

Similar to adding items but in revers 

> remove_item('Baked Beans', 2)
This will remove 2 x Baked Beans 

### Checking out 

When checking out, the checkout function will apply any applicable discounts, in this case on Sardines and Baked Beans. 

> checkout() 

This will check for items that can be discounted, if there is anything to be discounted it will be applied here


