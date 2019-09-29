catalogue = {
              'Baked Beans' : 0.99,
              'Biscuits' : 1.20,
              'Sardines' : 1.89,
              'Shampoo (Small)' : 2.00,
              'Shampoo (Medium)' : 2.50,
              'Shampoo (Large)' : 3.50
              }

items_on_offer = {
    'Baked Beans' : 'buy_2_get_1',
    'Sardines' : 'save_25%'
}

def discount(items, catalogue):
    discount = 0 
    for item in items:
        if item in items_on_offer:
            quantity = items[item]
            price = catalogue[item]
            if items_on_offer[item] == 'buy_2_get_1':
                discount += (quantity - (quantity % 3) )/3 * price
            if items_on_offer[item] == 'save_25%':
                discount += (quantity * price * 0.25 )
    return discount

