from datetime import datetime
import sqlite3


DATASOURCE = "/data/iot.db"

LOG_INSERT_QUERY = "insert into sensor_log (sensor_id, time, measure) values (?, ?, ?)"
LOG_READ_QUERY = "select sensor_id, time, measure from sensor_log where sensor_id = (?)"


def post(sensor_id:int, time:str, measure:str) -> dict:
    try:
        with sqlite3.connect(DATASOURCE) as con:
            con.execute(LOG_INSERT_QUERY, [sensor_id, time, measure])
        return {"success":1}
        
    except Exception as e:
        print(e)
        return {"success":0}


def get(sensor_id:int) -> dict:
    try:
        with sqlite3.connect(DATASOURCE) as con:
                cur = con.execute(LOG_READ_QUERY, [sensor_id])
                rows = cur.fetchall()
                result = {}
                for i, row in enumerate(rows):
                    result[i] = {"sensor_id":row[0], "time":row[1], "measure":row[2]}
        return result

    except Exception as e:
        print(e)
        return {"success":0}


