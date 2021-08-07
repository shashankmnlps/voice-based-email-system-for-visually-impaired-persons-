import mysql.connector


def con():
    mydb = mysql.connector.connect(
        username="root",
        password="1234",
        host="localhost",
        database="email",
        buffered=True
    )
    return mydb