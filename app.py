from flask import Flask, render_template, request, jsonify,redirect
from dbhelper import DBhelper
import mysql.connector

app = Flask(__name__)
# connect to the
conn=mysql.connector.connect(host="localhost",user="root",password="",database="minimini")
cursor=conn.cursor()
db1 = mysql.connector.connect(
    host="localhost",user="root",password="",database="minimini")
db=DBhelper()
user=""
@app.route('/register', methods=['POST'])
def handle_registration():
    username = request.json['username']
    global user
    user=username
    tableno = request.json['tableno']
    phn_no = request.json['phn_no']
    response =db.register(tableno,username,phn_no)
    if response == 1:
        print("Registration successful.")
    else:
        print("Registration failed.")


    return jsonify({'success': True})

@app.route('/welcome/<username>')
def welcome(username):
    data =db.menu()
    return render_template('index.html',data=data)

@app.route('/')
def index():
    return render_template('login.html')
@app.route("/welcome", methods=["POST"])
def welcomes():
    array_data = request.get_json()
    response = db.orders(user, array_data)
    if response == 1:
        print("Registration successful.")
    else:
        print("Registration failed.")

    # Return a success message if processing is successful
    return render_template('card.html')
@app.route('/adminlogin')
def admin():
    return render_template('adminlogin.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.json.get('username')
        password = request.json.get('password')
        data = db.search(username, password)
        if len(data) == 0:
            return jsonify({'success': False, 'message': 'Invalid username or password'})
        else:
            return jsonify({'success': True, 'message': 'Login successful'})

@app.route('/adminlogin/manager')
def manager():
    return render_template('manager.html')
@app.route('/cart')  # Initial route will show Orders
def orders():
    data1=db.cart(user)
    total=db.total(user)
    data={
        'order':data1,
        'tot':total[0][0]
    }
    return render_template('orders.html',data=data)
@app.route("/app.py", methods=["POST"])
def handle_payment():
  if request.method == "POST":
    payment= request.form.get("paymentMethod")
    username=user
    db.payment(payment,username)
    return f"Payment method '{payment}' received successfully!", 200
  else:
    return "Invalid request method", 405

# @app.route('/deleted/<int:user_id>', methods=['POST'])
# def deleted(user_id):
#     cursor = db1.cursor()
#     query = "DELETE FROM orders WHERE oprice = %s AND ouname = ''"
#     print(query)
#     cursor.execute(query, (user_id,))
#     db1.commit()
#     cursor.close()
#     return 'Deleted successfully!'
@app.route('/ordermanager')
def ordermanager():
    data=[]
    user_table=db.manageruser()
    order=db.manageorder(user_table)
    assign=db.managerassign(user_table)
    payment = []
    username = [inner_list[0] for inner_list in user_table]
    for user in username:
        cursor.execute(f"SELECT ptype,amount,status FROM payment WHERE pname='{user}'")
        data1 = cursor.fetchall()
        if len(data1) == 0:
            payment.append([f"{user}", (" ","0"," ")])
        else:
            payment.append([f"{user}", *data1])
    data2={
        'user_table':user_table,
        'orders':order,
        'assignto':assign,
        'total_pmod':payment
    }
    for dat in range(0,len(data2['user_table'])):
        data.append([f"{data2['user_table'][dat][0]}",f"{data2['orders'][dat][1:]}",f"{data2['user_table'][dat][1]}",f"{data2['total_pmod'][dat][1][1]}",f"{data2['total_pmod'][dat][1][0]}",f"{data2['assignto'][dat][0][0]}",f"{data2['total_pmod'][dat][1][2]}"])

    return render_template('ordermanager.html' ,data=data)

@app.route('/status/<int:user_id>', methods=['POST'])
def updatestatus(user_id):
    status="Delivered"
    cursor = db1.cursor()
    query = "UPDATE payment SET status = %s WHERE amount = %s"
    cursor.execute(query, (status, user_id))
    db1.commit()
    cursor.close()
    return 'Update successfully!'



@app.route('/transactions')
def transactions():
    info=db.transaction()
    total = db.tottransaction()
    data={
        'trans':info,
        'total':total
    }
    return render_template('transactions.html',data=data)

@app.route('/inventory')
def inventory():
    users = db.inventory()
    return render_template('inventory.html',users=users)

@app.route('/delete/<int:user_id>', methods=['POST'])
def delete(user_id):
    cursor = db1.cursor()
    query = "DELETE FROM inventory WHERE iid = %s"

    cursor.execute(query, (user_id,))
    db1.commit()
    cursor.close()
    return 'Deleted successfully!'

@app.route('/update/<int:user_id>')
def update(user_id):
    return render_template('update.html',user_id=user_id)
@app.route('/update',methods=['POST'])
def update_user():
    if request.method == 'POST':
        id = request.form['user_id']
        new_food = request.form['username']
        new_quantity= request.form['password']
        cursor = db1.cursor()
        query = "UPDATE inventory SET iname = %s, quantity = %s WHERE iid = %s"
        cursor.execute(query, (new_food, new_quantity, id))
        db1.commit()
        cursor.close()
        return 'Update successfully!'
if __name__ == '__main__':
    app.run(debug=True)
