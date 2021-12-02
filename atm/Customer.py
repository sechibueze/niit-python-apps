from db_config import customers_table_name
from db_manager import DB
customer_db = DB(customers_table_name)

class Customer:

    user = {}

    def __init__(self, user = {}):
        self.user = user
    def create_account(self, data):
        fullname = data.get('fullname')
        email = data.get('email')
        pin = data.get('pin')
        bal = data.get('balance')
        sql = 'INSERT INTO {}(fullname, email, pin, balance) VALUES (?, ?,?, ?)'.format(customers_table_name)
        payload = [fullname, email,pin, bal ]
        customer_db.create(sql, payload)
        print('Account created')
    def login(self, data):
        email = data.get('email')
        pin = data.get('pin')
        sql = "SELECT * FROM {} WHERE email = '{}' AND pin = '{}' LIMIT 1".format(customers_table_name, email, pin)
        user_list = customer_db.fetch(sql)
        if not user_list:
            return None
        formattted_user = self.format_user(user_list)
        self.set_user(formattted_user)
        return formattted_user
    def set_user(self, user):
        self.user = user
    def format_user(self, user_list):
        user_tup = user_list[0]
        user = {}
        user['id'] = user_tup[0]
        user['email'] = user_tup[1]
        user['fullname'] = user_tup[2]
        user['pin'] = user_tup[3]
        user['balance'] = user_tup[4]
        return user
    def get_customers(self):
        sql = 'SELECT * FROM {}'.format(customers_table_name)
    def withdraw(self, amount):
        print('Please wait for your transaction is processing...')
        new_bal = self.user.get('balance') - amount
        self.update_balance(new_bal)
        print('Thank you for banking with us')
        print('Please take your cash...')
    def update_balance(self, amount):
        sql = "UPDATE {} SET balance = {} WHERE email = '{}'".format(customers_table_name, amount, self.user.get('email'))
        customer_db.run_query(sql)
        email = self.user.get('email')
        pin = self.user.get('pin')
        login = {
            "email": email,
            "pin": pin
        }
        self.login(login)
    def deposite(self, amount):
        new_bal = self.user.get('balance') + amount
        self.update_balance(new_bal)
    def get_report(self):
        mesage = "Hello {}, Your current balance is now {}".format(self.user.get('fullname'), self.user.get('balance', 0))
        return mesage