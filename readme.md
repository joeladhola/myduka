INTRODUCTION TO FLASK

What is pip? - package installer for Python...installs additional libraries /modules not included in the Python standard library
Library - collection of functions designed to perform specific tasks

pip is a command
pip show - to see what you've installed e.g
pip show flask

pip list - lists every python module installed with pip

developer builds web application,deploy it online, application is assigned a unique IP address(resource locator)
domain name - a much simpler way for users to access applications online - DNS -142.251.47.142->www.google.com


1.create a database
2.create tables and their relationships

build a Point Of Sale System - e.g Naivas, Carrefour

1.psycopg2
- is a posgresql adapter for python. - its a driver  - connects your code to a database
- allows your python code to interact with a postgresql database  - run sql queries, fetch data, insert data e.t.c using Python

CRUD Operations
C- create  - insert
R- read    - select
U- update  - update
D- delete  - delete

psql 

psql -U posgres
server name - localhost
port - 5432
password - yourpassword

Prerequisite -> SQL queries


HTML/CSS/JS --------- Python ----------- SQL
(Interface) <flask> (Server) <psycopg2>(Database)


1. create a database
2. create tables and enforce relationships and constraints


- Limit direct database acccess

2 files - main.py  --> server -> flask
        - database.py --> database -> connects to postgreSql -> psycopg2

#library && framework

once you install packages/ modules/ dependencies
-->they are stored in your global environment

conn -> establishes connection to the database
cur -> object used to execute sql queries -> perform db operations

N/B
1. use cursor to fetch data from our database
  data format --> list of tuples


  TASK;
  #insert a sale using psql and view the sales using psycopg2
  #use functions


  Inserting Data
  1. Inserting Products with Psycopg2
  --> insert query
  --> insert into table_name(columns)values(actual_values)

- write your insert query to insert data into your database
- execute query with cursor
- commit your data to the database

"insert into products(name,buying_price,selling_price)values('eggs',15,20)"
quotations - represent starting & ending point


# push to GitHub everyday
Library - collection of functions provided by the programming language to perform specific tasks
datetime - current date and time


main.py - server
database.py - database operations


FRAMEWORK VS LIBRARIES
- Concept of building a house

method 1:
- Mo wants to build
- decides he'll do entire process himself.
- gets all required tools necessary for the building designs the house and stores them in a store
- does the actual building process from ground up all the way to completion
- he's responsible for his own design and the process including how its build and how long it takes
-> flexibility

method 2
- Oi wants to build
- acknowledges that she doesnt have the expertise to build this house herself
- seeks the help of professionals to build the house
- architect, engineer, construction manager, tehnical workforce,e.t.c
- each of them tells him whats required for building process

2 -> simpler but not flexible ---- library
1 -> longer complicated but flexible ---- framework






Framework - structured foundation for application development that decides how you build applications
- has strict guidelines on usage
    examples of frameworks;
    1. Python - flask, django, FastAPI
    2. NodeJs - express
    3. Java - spring
    4. C# - .NET
    5. Ruby - ruby on rails 




Library - reusable code used to perform specific tasks
- flexible
- usage depends on the developer
    examples of libraries:
    1. Bootstrap
    2. Numpy - computation
    3. Panda - data analysis
    4. Tensor flow - ML
    5. Matplotlib - data visualisation


FLASK FRAMEWORK
1. Routing
- mechanism to map URLs to Python functions -> system for resource navigation. 
- Connects URL to a function in your Flask app
- When a user visits  a specific URL, flask knows which function to run - function is called a view function

1. URL - full address used to access resources on the we e.g www.techcamp.co.ke
2. Route - part of the URL used to access a specific resource e.g /dashboard /home


Client(browser) <-------> Routing <------> function containing resources and data e.g products and sales


classes and objects

class Student
name 
age 
course

Student Trevor

OOP -> object Oriented Programming


app = Flask(__name__) - creates an instance of a flask app

__name__ -> special built in variable representing the name of the current file
-> helps flask know where your application starts and also where to find other resources

To create a route using Flask we use @app.route() decorator

a decorator -> is a function that decides or modifies the behavior of another function
-> usually have the '@' character before the function

http://127.0.0.1:5000  - url

127.0.0.1 -> localhost
5000 -> port

@app.route('/') -> decorator function responsible for routing


def home():  _ vie function
    return "Alchemist Mo"

/- index



@app.route() - decorator function -> can take some parameters

1. Rule -> defines a path a user takes / access in the browser e.g /, /name, /products
2. Endpoint -> name of the view function ->  name Flask uses to identify the route internally


return -> get back some data from the function and terminate

Task
1. create 3 routes and return 3 different data values and test them in your browser
2. In your project folder create two folders
a) templates
b) static

watcher -> checking for any changes in your application and reloading it


To return/ render html pages we need to have the templates and static folder
The folders have to have that exact casing and spelling

render -> serve a html page with flask
Goal: display a html page using flask
templates -> all your html files
           -> all html files MUST be here

static -> all static files - files that dont change much
       -> css files
       -> images
       -> js files
       -> favicon
       -> fonts, pdf files

To render html pages using Flask, we use functions provided by Flask
  render_template() - function
  -you have to import it from flask
  -render_template() -> can take some parameters
  1. full name of a html page
  2. variables

  Jinja -> templating engine integrated with Flask to render dynamic HTML pages

  * jinja is just syntax
  how to use Jinja with variables:

  TAsk;
  Create this routes
  1. products
  2. sales
  3. dashboard
  4. login
  5. register
  They shld all return their html pages
  in each of those routes render a random variable of your choice using Jinja



  JINJA -> templating engine integrated with Flask to render dynamic HTML pages
  -> dosplay our data from Python in HTML

  HOW IT WORKS
  1. Templates - predefined HTML files - define Jinja sntax here with placeholders e.g variables
  2. Data - application provides the data - variables
  3. Rendering - Jinja processes the template and replaces the placeholders with actual data

  JInja Syntax
  1. variables - {{}}
  e.g name = "Jane Doe"
      {{name}}
  2. Logic / Control Structures {% %}
  - for control structures 
  a) initialise it
  b) write logic
  c) end it _ terminate the control structure

  {% if x == 10 %}
     //logic goes here
  {% end if%} --- terminate control structure
  





  Control Structures in Programming
  --> Way to specify flow of control in Programs

  1. Sequential flow / Sequential Logic
  - Instructions follow a sequential order usually top to bottom

  2. Selection 
  - Conditional statements - decision makers - if else
  
  3. Iteration
  - looping - executing an instruction until a condition is met - for while




TASK
1. Get a Bootstrap Navbar- cdn files-->css,js
2. Get a Bootstrap styled table - 4columns-> id,product_name, buying_price, selling_price

- display products in that table




TASK
** build the navbar
display sales data using a Bootstrap table on sales page
--> stock before sales



Get a Bootstrap modal.. in that modal have a form with input fields... product name, buying price, selling price


POSTING DATA
Posting - sending information from a client (e.g web browser) to server processing and storage
Client - an entity that sends a HTTP rquest to a server

Data flow

1. User visits a route in your application - flask will route
2. User fills out a form and submits the form
3. Flask will find a route to execute a function using specified info from the form
4. Once route is found, Flask extracts data from the form using request.form, validates and saves it
5. User is directed


Request 
-> An object from request class that provides access to data from a HTTP request
- it contains all details about the request made by the client
- allows you to:
1. access data sent by the client e.g form data
2. allow you to work with http methods

HTTP methods - a way of telling a server what to do with data
1. GET - get data
2. POST - send data 
3. PUT - updating data
4. DELETE - getting rid from data

request.method - gives you the http method from the client
request.form - allows you to access form data from the client for processing

- data is coming in string form in key value pairs
- retrieves form data using keys

1. without modal
2. with modal


Checklist in posting data
1. correct input type
2. action - route - where should my form data be taken
3. method - what the Server should do with form data

4. name - key used by request.form to extract form values
5. button type submit

HTTP status codes - 3 digit numbers returned by a server to indicate the result of a request
starting with:
1 - Informational
2 - Success
3 - Redirection
4 - Client error
5 - Server error


Remarks:
1. url_for() takes the name of the view function as a parameter and not the route name
2. not every single route is return a html page


POST STOCK ->
We have our product data -
sales table is exactly like stock table


TASK
Implement Making Sale
Hint: - making a sale is  exactly like adding stock
**
Use data tables for your products and sales data 


Make a Sale
To only make sales if we have enough stock

to make sales and update stock

task;
- attempt to update stock after making sale
- only make sales if you have enough stock
- write the following sql queries in python ;
1. sales per day
2. sales per product
3. profit per day
4. profit per product

sales per product
- sales - product
foreign key - a primary key in another table used to link tables

select products.name,sum(sales.quantity * products.seling_price) as revenue from products join sales
on products.id = sales.pid group by(products.name);

HINT: for per day
date.function