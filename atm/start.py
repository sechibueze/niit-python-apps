from offers import offers
from Customer import  Customer

def require_login():
    email = input("Email ")
    pin = input("Pin ")
    data = {
        "email": email,
        "pin": pin
    }
    customer = Customer()
    logged_in_user = customer.login(data)
    if not logged_in_user:
        print('Login failed')
        logged_in_user = require_login()
    return logged_in_user

def start_withdrawal():
    user = require_login()
    amount = input("How much to withdraw")
    customer = Customer(user)
    customer.withdraw(int(amount))
    print(customer.get_report())

def start_deposit():
    user = require_login()
    print(' user',user)
    customer = Customer(user)
    amount = input("How much to deposite")
    print('customer user', customer.user)
    customer.deposite(int(amount))
    print(customer.get_report())

def collect_account_data():
    fullname = input("Name ")
    email = input("Email ")
    pin = input("Pin ")
    data = {
        "fullname": fullname,
        "email": email,
        "pin": pin,
        "balance": 10000
    }
    customer = Customer()
    customer.create_account(data)

print("Welcome to NIIT Bank")
for offer in offers:
    id = offer.get('id')
    name = offer.get('name')
    print('{} : {}'.format(id, name))
selected_offer_id = input("Choose a service")

if selected_offer_id == '1':
    start_withdrawal()
elif selected_offer_id == '2':
    start_deposit()
elif selected_offer_id == '3':
    collect_account_data()
else:
    print("No offer found")
