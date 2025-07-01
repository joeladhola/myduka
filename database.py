import psycopg2 

conn = psycopg2.connect(user="postgres",password="0209",host="localhost",port="1934",database="mydukaa")

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


def insert_sales(values):
    sales_query= "insert into sales(pid,quantity,created_at)values(%s,%s,now())"
    cur.execute(sales_query,values)
    conn.commit()


def insert_stock(values):
    stock_query= "insert into stock(pid,stock_quantity,created_at)values(%s,%s,now())"
    cur.execute(stock_query,values)
    conn.commit()

def get_stock():
    cur.execute("select * from stock;")
    stock = cur.fetchall()
    return stock

stock = get_stock()


def sales_per_product():
    cur.execute("""
     select products.name,sum(sales.quantity * products.selling_price) as revenue from products join sales
on products.id = sales.pid group by(products.name);

""")
    sales_product = cur.fetchall()
    return sales_product


def profit_per_product():
    cur.execute("""
select products.name,sum(sales.quantity * (products.selling_price - products.buying_price)) as daily_profit from products join sales
on products.id = sales.pid group by(products.name);
""")
    profit_product = cur.fetchall()
    return profit_product


def sales_per_day():
    cur.execute("""
select date(sales.created_at) as date, sum(sales.quantity * products.selling_price) as sales from sales join products on products.id = sales.pid group by date order by date asc;
""")
    sales_day = cur.fetchall()
    return sales_day


def profit_per_day():
    cur.execute("""
select date(sales.created_at) as date, sum(sales.quantity * (products.selling_price - products.buying_price)) as sales from sales join products on products.id = sales.pid group by date order by date asc;
""")
    profit_day = cur.fetchall()
    return profit_day


def available_stock(pid):
    cur.execute("select sum(stock.stock_quantity) from stock where pid = %s",(pid,))
    total_stock = cur.fetchone()[0] or 0

    cur.execute("select sum(sales.quantity) from sales where pid =%s",(pid,))
    total_sold = cur.fetchone()[0] or 0
    return total_stock - total_sold


def check_user(email):
    cur.execute("select * from users where users.email = %s",(email,))
    user = cur.fetchone()
    return user


def insert_user(user_details):
    cur.execute("insert into users(full_name,email,phone_number,password)values(%s,%s,%s,%s)",(user_details))
    conn.commit()

    
