import psycopg2


def connectDB():
    con = psycopg2.connect(
        database="lizy", 
        user="postgres", 
        password="passwordhere", 
        host="127.0.0.1", 
        port="5432")
    cursor = con.cursor()

    return con, cursor


connectDB()