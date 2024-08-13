import pymysql

try:
    conn = pymysql.connect(host='localhost', user='root', password='', database='ridesharing')
    print("Connected to the database successfully!")
    conn.close()
except pymysql.MySQLError as e:
    print(f"Error connecting to the database: {e}")
