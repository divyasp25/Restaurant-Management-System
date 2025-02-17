import mysql.connector
import sys

class DBhelper:
    def __init__(self):
        try:
            self.conn=mysql.connector.connect(host="localhost",user="root",password="",database="minimini")
            self.mycursor=self.conn.cursor()
        except:
            print("Some error occured.Could not connect to database")
            sys.exit(0)
        else:
            print("Connected to database")
    def register(self,tableno,username,userphone):
        try:
            self.mycursor.execute("""
            INSERT INTO `users` (`table_no`, `uname`, `uphone`) VALUES ('{}', '{}', '{}');
            """.format(tableno,username,userphone))
            self.conn.commit()
        except Exception as e:
            print("Error:", e)

            return -1
        else:
            return 1
    def search(self,username,password):
        self.mycursor.execute("""
        SELECT * FROM `employee` WHERE ename LIKE '{}' AND password LIKE '{}' AND erole LIKE 'manager'
        """.format(username,password))
        data=self.mycursor.fetchall()
        return data

    def menu(self):
        # Fetch data from the food table
        self.mycursor.execute("SELECT * FROM food")
        data = self.mycursor.fetchall()  # Fetch all rows
        return data

    def orders(self,username,menu):
        for food in menu:
            self.mycursor.execute(f"SELECT fprice FROM food WHERE fname='{food}'")
            price = self.mycursor.fetchall()
            self.mycursor.execute("""
            INSERT INTO `orders` (`ouname`, `ofname`, `oprice`) VALUES ('{}', '{}', '{}');
            """.format(username,food,price[0][0]))
            self.conn.commit()
        return 1
    def total(self,user):
        self.mycursor.execute(f"SELECT SUM(oprice) FROM orders WHERE ouname='{user}'")
        data = self.mycursor.fetchall()
        return data

    def payment(self,payment_method,user):
        self.mycursor.execute(f"SELECT SUM(oprice) FROM orders WHERE ouname='{user}'")
        total = self.mycursor.fetchall()
        self.mycursor.execute("""
                    INSERT INTO `payment` (`pname`, `ptype`, `amount`) VALUES ('{}', '{}', '{}');
                    """.format(user, payment_method, total[0][0]))
        self.conn.commit()

    # def transactionslrno(self):
    #     self.mycursor.execute(f"SELECT pid FROM payment")
    #     data = self.mycursor.fetchall()
    #     return data
    def tottransaction(self):
        self.mycursor.execute(f"SELECT SUM(oprice) FROM orders")
        data = self.mycursor.fetchall()
        return data
    def cart(self,user):
        self.mycursor.execute(f"SELECT ofname,oprice FROM orders WHERE ouname='{user}'")
        data = self.mycursor.fetchall()
        return data
    def inventory(self):
        self.mycursor.execute("""
                SELECT * FROM `inventory`
                """)
        data = self.mycursor.fetchall()
        return data

    def delete(self,userid):
        self.mycursor.execute("""
            DELETE FROM `inventory` WHERE uid = {};
        """.format(userid))

        # Commit the changes to the database
        data=self.mydb.commit()
        return data

    def manageruser(self):
        self.mycursor.execute(f"SELECT uname,table_no FROM users")
        data = self.mycursor.fetchall()
        return data
    def managerassign(self,username):
        assign= []
        table = [inner_list[1] for inner_list in username]
        for tableno in table:
            self.mycursor.execute(f"SELECT ename FROM employee WHERE eid='{tableno}'")
            data = self.mycursor.fetchall()
            if len(data) == 0:
                assign.append(" ")
            else:
                assign.append(data)
        return assign
    def manageorder(self,username):
        order=[]
        username= [inner_list[0] for inner_list in username]
        for user in username:
            self.mycursor.execute(f"SELECT ofname FROM orders WHERE ouname='{user}'")
            data = self.mycursor.fetchall()
            if len(data)==0:
                order.append([f"{user}","Order not placed"])
            else:
                order.append([f"{user}", *[inner_list[0] for inner_list in data]])
        return order

    def managepayment(self,username):
        payment = []
        username = [inner_list[0] for inner_list in username]
        for user in username:
            self.mycursor.execute(f"SELECT ptype,amount,status FROM payment WHERE pname='{user}'")
            data = self.mycursor.fetchall()
            if len(data) == 0:
                payment.append([f"{user}", " "])
            else:
                payment.append([f"{user}", *data])
        return payment

    def transaction(self):
        self.mycursor.execute(f"SELECT DATE(pdate) AS date, SUM(amount) AS total_amount FROM payment GROUP BY DATE(pdate)")
        data = self.mycursor.fetchall()
        return data