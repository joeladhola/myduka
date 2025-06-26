from flask import Flask, render_template, request, redirect, url_for, flash
from database import get_products, get_sales,insert_sales, insert_products, insert_stock, get_stock, available_stock, sales_per_day, sales_per_product, profit_per_day, profit_per_product

#creating a Flask instance
app = Flask(__name__)

app.secret_key = 'ma2111jo0209'

@app.route('/')
def home():
    flash("Accessed Home Page","success")
    return render_template("index.html")

@app.route('/products')
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
def dashboard():
    sales_product = sales_per_product()
    profit_product = profit_per_product()
    sales_day = sales_per_day()
    profit_day = profit_per_day()

    #product related dash data
    product_names = [i[0] for i in sales_product]
    sales_prod = [i[1] for i in sales_product]
    prof_prod =[i[1] for i in profit_product]

    #date related dash data
    date = [i[0] for i in sales_day]
    sales_of_day = [i[1] for i in sales_day]
    profit_of_day = [i[1] for i in profit_day] 

    return render_template("dashboard.html",
                           product_names = product_names,
                           sales_prod=sales_prod,
                           prof_prod = prof_prod,
                           date=date,
                           sales_of_day=sales_of_day,
                           profit_day=profit_of_day)

@app.route('/login')
def login():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    return render_template("login.html",numbers=numbers)

@app.route('/register')
def register():
    return render_template("register.html")






app.run(debug=True)  