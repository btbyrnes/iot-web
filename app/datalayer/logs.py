from datetime import datetime
import sqlite3
import json

DATASOURCE = "/data/iot.db"

LOG_INSERT_QUERY = "insert into sensor_log (db_id, sensor_id, time, measure) values (?, ?, ?, ?)"
LOG_READ_QUERY = "select db_id, sensor_id, time, measure from sensor_log where sensor_id = (?)"


def post_log(db_id:int, sensor_id:int, time:str, measure:str) -> dict:
    try:
        with sqlite3.connect(DATASOURCE) as con:
            con.execute(LOG_INSERT_QUERY, [db_id, sensor_id, time, measure])
        return {"success":1}
        
    except Exception as e:
        print(e)
        return {"success":0}


def get_log(db_id:int) -> dict:
    try:
        with sqlite3.connect(DATASOURCE) as con:
                cur = con.execute(LOG_READ_QUERY, [69])
                rows = cur.fetchall()
                result = {}
                for i, row in enumerate(rows):
                    result[i] = {"db_id":row[0], "sensor_id":row[1], "time":row[2], "measure":row[3]}
        return result

    except Exception as e:
        print(e)


