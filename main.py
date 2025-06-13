from flask import Flask

#creating a Flask instance
app = Flask(__name__)

@app.route('/')
def home():
    return "Alchemist Mo"


@app.route('/name')
def name():
    return "My name is Joel"


@app.route('/about')
def about():
    return "About Joel"


@app.route('/service')
def service():
    return "Services offered by Joel"


@app.route('/more')
def more():
    return "More about Joel"



app.run()  