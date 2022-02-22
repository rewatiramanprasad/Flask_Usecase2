import psycopg2
import json

config = open("config/config.json", "r").read()
data=json.loads(config)

def connect():
    con = psycopg2.connect(
        host=data["ip"],
        database=data["database"],
        user=data["user"],
        password=data["password"])
    return con


def execute(query):
    con = connect()
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    cur.close()
    con.close()


def execute_fetchall(query):
    con = connect()
    cur = con.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    con.close()
    return data
