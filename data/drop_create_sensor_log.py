import sqlite3
import json

DATASOURCE = "data/iot.db"

def main():
    with open("data/create_sensor_log.sql", "r") as f:
        create_query = f.read()

    query("drop table sensor_log")
    query(create_query)

    with open("data/create_sensors.sql", "r") as f:
        create_query = f.read()
    
    query("drop table sensors")
    query(create_query)

    query("insert into sensors (db_id, sensor_id, name, type, status) values (1,1,'None','None',0)")

def query(query:str):
    with sqlite3.connect(DATASOURCE) as con:
        cur = con.execute(query)


if __name__ == "__main__":
    main()