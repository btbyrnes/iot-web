import sqlite3

DATASOURCE = "data/iot.db"

def query(query:str=None):
    if query is None:
        query = "select * from sensors"
    with sqlite3.connect(DATASOURCE) as con:
        cur = con.execute(query)
    print(cur.fetchall())

if __name__ == "__main__":
    query("select * from sensor_log")