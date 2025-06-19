import psycopg2 

conn = psycopg2.connect(user="postgres",password="0209",host="localhost",port="1934",database="mydukaa")

#from datetime import datetime
cur = conn.cursor()


def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products


def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales






def insert_products(values):
    insert_query ="insert into products(name,buying_price,selling_price)values(%s,%s,%s)"
    cur.execute(insert_query,values)
    conn.commit()

#product_values1 = ('jacket',2500,3000)
#product_values2 = ('phone',15000,20000)

#insert_products(product_values1)
#insert_products(product_values2)

#product_data = get_products()
#print (product_data)


def insert_sales(values):
    sales_query= "insert into sales(pid,quantity,created_at)values(%s,%s,%s)"
    cur.execute(sales_query,values)
    conn.commit()


sales_values1 = (8,26,'now()')
sales_values2 = (9,33,'now()')

insert_sales(sales_values1)
insert_sales(sales_values2)

sales_data = get_sales()


    
