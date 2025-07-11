from flask import Flask, render_template, request, redirect, url_for, flash, session
from database import get_products, get_sales,insert_sales, insert_products, insert_stock, get_stock, available_stock, sales_per_day, sales_per_product, profit_per_day, profit_per_product, check_user, insert_user
from flask_bcrypt import Bcrypt
# use capital B in bycrpt
from functools import wraps

#creating a Flask instance
app = Flask(__name__)

app.secret_key = 'ma2111jo0209'

bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template("index.html")

def login_required(f):
    @wraps(f)
    def protected(*args,**kwargs):
        if 'email' not in session:
            return redirect(url_for('login'))
        return f(*args,**kwargs)
    return protected

@app.route('/products')
@login_required
def prod():
    products = get_products()
    return render_template("products.html",products=products)

@app.route('/add_products', methods=['GET','POST'])
def addprods():
    product_name = request.form["product_name"]
    buying_price = request.form["buying_price"]
    selling_price = request.form["selling_price"]
    new_products = (product_name,buying_price,selling_price)
    insert_products(new_products)
    flash("Product inserted successfully",'success')
    return redirect(url_for('prod'))



@app.route('/sales')
@login_required
def sales():
    products = get_products()
    sales = get_sales()
    return render_template("sales.html",products=products,sales=sales)

@app.route('/add_sales', methods=['GET','POST'])
def add_sales():
    pid = request.form['pid']
    quantity = request.form['quantity']
    new_sales = (pid,quantity)
    stock_available = available_stock(pid)
    if stock_available < float(quantity):
        flash("Insufficient stock to complete sale","danger")
        return redirect(url_for('sales'))
        
    insert_sales(new_sales)
    flash("Sale made successfully",'success')
    return redirect(url_for('sales'))


@app.route('/stock')
@login_required
def stock():
    products = get_products()
    stock = get_stock()
    return render_template("stock.html",products=products,stock=stock)


@app.route('/add_stock', methods=['GET','POST'])
def add_stock():
    pid = request.form['pid']
    stock_quantity = request.form['stock']
    new_stock = (pid,stock_quantity)
    insert_stock(new_stock)
    flash("Stock added successfully",'success')
    return redirect(url_for('stock'))


@app.route('/dashboard')
@login_required
def dashboard():
    sales_product = sales_per_product()
    profit_product = profit_per_product()
    sales_day = sales_per_day()
    profit_day = profit_per_day()

    #product related dash data
    product_names = [i[0] for i in sales_product]
    sales_prod = [float(i[1]) for i in sales_product]
    prof_prod =[float(i[1]) for i in profit_product]

    #date related dash data
    date = [str(i[0]) for i in sales_day]
    sales_of_day = [float(i[1]) for i in sales_day]
    profit_of_day = [float(i[1]) for i in profit_day] 

    return render_template("dashtest.html",
                           product_names = product_names,
                           sales_prod=sales_prod,
                           prof_prod = prof_prod,
                           date=date,
                           sales_of_day=sales_of_day,
                           profit_day=profit_of_day)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user = check_user(email)
        if not user: 
            flash("User not found,please register!","danger")
        else:
            if bcrypt.check_password_hash(user[-1],password):
                flash("Logged in",'success')
                session['email'] = email
                return redirect(url_for('dashboard'))
            else:
                flash("Password incorrect",'danger')
    return render_template("login.html")

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        phone_number = request.form['phone']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = check_user(email)
        if not user:
            new_user = (full_name,email,phone_number,hashed_password)
            insert_user(new_user)
            flash("User registerd successfully","success")
            return redirect(url_for('login'))
        else:
            flash("User already exists,please login","danger")
    return render_template("register.html")


@app.route('/logout')
@login_required
def logout():
    session.pop('email',None)
    flash("Logged out",'info')
    return redirect(url_for('login'))



app.run(debug=True)  