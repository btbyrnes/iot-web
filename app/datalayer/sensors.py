from datetime import datetime
import logging
import sqlite3
import json

DATASOURCE = "/data/iot.db"

GET_SENSOR_QUERY_SENSOR_ID = "select db_id, sensor_id, name, type, status from sensors where sensor_id=(?)"
GET_SENSOR_QUERY_DB_ID = "select db_id, sensor_id, name, type, status from sensors where db_id=(?)"

CREATE_SENSOR_QUERY = "insert into sensors (db_id, sensor_id, name, type, status) values(?, ?, ?, ?, ?)"
DELETE_SENSOR_QUERY = "delete from sensors where sensor_id=(?)"

GET_SENSORS_QUERY = "select db_id, sensor_id, name, type, status name from sensors where db_id > 1"

GET_MAX_DB_SENSOR_ID = "select max(db_id) from sensors"


def post(sensor_id:int, name:str, sensor_type:str, status:str) -> dict:
    try:
        db_id = get_new_db_id()
        with sqlite3.connect(DATASOURCE) as con:
            con.execute(CREATE_SENSOR_QUERY, [db_id, sensor_id, name, sensor_type, status])
            results = {"db_id": db_id}
            return results
    except Exception as e:
        return {"db_id": -1}


def get(sensor_id:int=None, db_id:int=None) -> dict:
    sensors = 0
    with sqlite3.connect(DATASOURCE) as con:
        if sensor_id is not None:
            sensors = con.execute(GET_SENSOR_QUERY_SENSOR_ID, [sensor_id])
        if db_id is not None:
            sensors = con.execute(GET_SENSOR_QUERY_DB_ID, [db_id])
        elif sensor_id is None and db_id is None:
            sensors = con.execute(GET_SENSORS_QUERY)
    
    sensors = sensors.fetchall()

    results = {}
    for i, sensor in enumerate(sensors):
        results[i] = {"db_id":sensor[0],"sensor_id":sensor[1],"name":sensor[2],"type":sensor[3],"status":sensor[4]}

    return results


def delete(sensor_id:int, name:str=None) -> dict:
    try:
        with sqlite3.connect(DATASOURCE) as con:
            con.execute(DELETE_SENSOR_QUERY, [sensor_id])
        return {"success":1}
    except Exception as e:
        print(e)
        return {"success":0}

UPDATE_SENSOR_QUERY = "update sensors set status = (?) where sensor_id = (?)"
def put(sensor_id:int, status:str) -> dict:
    try:
        with sqlite3.connect(DATASOURCE) as con:
            cur = con.cursor()
            cur.execute(UPDATE_SENSOR_QUERY, [status, sensor_id])
        return {"success":1}
    except Exception as e:
        print(e)
        return {"success":0}


def get_new_db_id() -> int:
    try:
        with sqlite3.connect(DATASOURCE) as con:
            cur = con.execute(GET_MAX_DB_SENSOR_ID)
        results = cur.fetchall()
        max_id = results[0][0]
        return max_id + 1
    except Exception as e:
        print(e)
        pass
    

if __name__ == "__main__":
    pass