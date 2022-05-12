from datetime import datetime
import requests
import logging
import time

import sqlite3
import json

DATASOURCE = "data/iot.db"

URL = "http://192.168.1.86:5050"

URL_DICT = {
    "1":"sensor",
    "2":"control"
}


if __name__ == "__main__":

    # ## API Test post a sensor
    # r = requests.post(URL + "/" + "sensor", params={"sensor_id":69, "name":"test", "type":1})
    # print(r.json())
    # db_id = r.json()["db_id"]

    ## API Test get a sensor # Change to Sensor ID
    r = requests.get(URL+"/"+"sensor", params={"db_id":2})
    # logging.debug(r.json())
    # print(r.json())

    # ## API Test post a log
    # payload = {"db_id":3, "sensor_id":10, "time":1, "measure":1}
    # r = requests.post(URL + "/" + "log", params=payload)
    # print(r.json())


    # ## Test sustained logging
    # for i in range(0,10):
    #     t = str(datetime.now())
    #     db_id = 86
    #     sensor_id = 69
    #     payload = {"db_id":db_id, "sensor_id":sensor_id, "time":t, "measure":100+i}
    #     r = requests.post(URL+"/log", params=payload)
    #     print(r.json())
    #     time.sleep(3)


    # ## FUNCTIONAL test of read logs
    # LOG_READ_QUERY = "select db_id, sensor_id, time, measure from sensor_log where sensor_id = (?)"
    # with sqlite3.connect(DATASOURCE) as con:
    #     cur = con.execute(LOG_READ_QUERY, [69])
    #     rows = cur.fetchall()
    #     results = {}
    #     for i, row in enumerate(rows):
    #         results[i] = {"db_id":row[0], "sensor_id":row[1], "time":row[2], "measure":row[3]}
    #     print(results)

  
    # ## Functional test of the db
    # SENSORS_READ_QUERY = "select * from sensors"

    # with sqlite3.connect(DATASOURCE) as con:
    #     cur = con.execute(SENSORS_READ_QUERY)
    #     print(cur.fetchall())

    # ## API test of get all sensors
    # r = requests.get(URL+"/sensors")
    # print(r.json())

    ## API Test of not finding a sensor
    payload = {"sensor_id":69}
    r = requests.get(URL+"/sensor", params=payload)
    print(r.json())
    
    pass