from flask import Flask, render_template

#creating a Flask instance
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/products')
def prod():
    product = "eggs"
    return render_template("products.html",data = product)


@app.route('/sales')
def sales():
    return render_template("sales.html")


@app.route('/about')
def about():
    return "About Joel"


@app.route('/service')
def service():
    return "Services offered by Joel"


@app.route('/more')
def more():
    return "More about Joel"



app.run(debug=True)  