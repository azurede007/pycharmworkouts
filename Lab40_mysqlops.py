import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def createconnection():
    conn = None
    try:
        conn = mysql.connector.connect(host=os.getenv("MYSQL_SERVERNAME"),
                                       user=os.getenv("MYSQL_USERNAME"),
                                       password=os.getenv("MYSQL_PASSWORD"),
                                       database=os.getenv("MYSQL_DBNAME"))
    except Exception as e:
        print("Error:", e)

    return conn

def getalldatabases(con):
    print("===Database List===")
    cursor = con.cursor()
    cursor.execute("SHOW DATABASES")
    dbs = cursor.fetchall()
    for db in dbs:
        print(db)
    cursor.close()

def getalltables(con):
    cursor = con.cursor()
    cursor.execute("SHOW TABLES")
    tbls = cursor.fetchall()
    print("===Table List===")
    for t in tbls:
        print(t)
    cursor.close()


def gettabledata(con,tablename):
    cursor = con.cursor()
    cursor.execute(f"select * from {tablename}")
    customers = cursor.fetchall()
    print(f"===Table Data:{tablename}===")
    for c in customers:
        print(c)
    cursor.close()


def insertcustomerdata(con,custid,fname,lname,age,prof):
    cursor = con.cursor()
    cursor.execute(f"insert into tblcustomer values({custid},'{fname}','{lname}',{age},'{prof}')")
    cursor._connection.commit()
    cursor.close()
    print("===Record Inserted===")

conn = createconnection()
getalldatabases(conn)
getalltables(conn)
gettabledata(conn,"tblcustomer")
insertcustomerdata(conn,1004,"Irfan","Kader",35,"Teacher")