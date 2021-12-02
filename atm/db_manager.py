from db_setup import cursor, connection

class DB:
    def __init__(self, table_name):
        self.table = table_name
    def find_all(self):
        sql = 'SELECT * FROM {}'.format(self.table)
        result = cursor.execute(sql)
        return result.fetchall()
    def find_by_id(self, key, value):
        sql = "SELECT * FROM {} WHERE {} = '{}'".format(self.table, key, value)
        result = cursor.execute(sql)
        return result.fetchall()
    def fetch(self, sql):
        result = cursor.execute(sql)
        return result.fetchall()
    def run_query(self, sql):
        res = cursor.execute(sql)
        connection.commit()
        return res


    def create(self, sql, payload):
        cursor.execute(sql, payload)
        connection.commit()
        return True


db = DB('customers')
# db.create(sql, payload)

data = db.find_by_id('email', 'wise@niit.com')
print(data)
# for pin in data.fetchall():
#     print(pin)
