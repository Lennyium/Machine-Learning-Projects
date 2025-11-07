import codecademylib3
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

visits_cart = pd.merge(visits, cart, how='left')
print(len(visits_cart))
total_visits = len(visits_cart)

print(len(visits_cart[visits_cart.isnull()]))
no_cart = len(visits_cart[visits_cart['cart_time'].isnull()])
percent_no_cart = float(no_cart) / total_visits * 100
print(percent_no_cart)

cart_checkout = pd.merge(cart, checkout, how='left')
total_cart = len(cart_checkout)
no_checkout = len(cart_checkout[cart_checkout['checkout_time'].isnull()])
percent_no_checkout = float(no_checkout) / total_cart * 100
print(percent_no_checkout)

all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')
print(all_data.head())

reached_checkout = len(all_data[all_data['checkout_time'].notnull()])
no_purchase = len(all_data[
    (all_data['checkout_time'].notnull()) &
    (all_data['purchase_time'].isnull())
])
percent_no_purchase = float(no_purchase) / reached_checkout * 100
print(percent_no_purchase)
# Visiting and adding to cart has the highest percentage of user not completing

all_data['time_to_purchase'] = all_data['purchase_time'] - all_data['visit_time']
print(all_data.time_to_purchase)
average_time_to_purchase = all_data.time_to_purchase.mean()
print(average_time_to_purchase)
