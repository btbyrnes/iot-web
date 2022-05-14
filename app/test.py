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

    ## API Test post a sensor
    r = requests.post(URL + "/" + "sensor", params={"sensor_id":69, "name":"test", "type":1, "status":0})
    print(r.json())
    r = requests.post(URL + "/" + "sensor", params={"sensor_id":71, "name":"test", "type":1, "status":0})
    print(r.json())

    ## API Test get a sensor
    for id in [69,71]:
        r = requests.get(URL+"/"+"sensor", params={"sensor_id":id})
        print(r.json())

    ## API Test post a log
    payload = {"db_id":3, "sensor_id":69, "time":1, "measure":1}
    r = requests.post(URL + "/" + "log", params=payload)
    print(r.json())


    ## Test sustained logging
    for i in range(0,10):
        t = str(datetime.now())
        sensor_id = 69
        payload = {"sensor_id":sensor_id, "time":t, "measure":100+i}
        r = requests.post(URL+"/log", params=payload)
        print(r.json())
        time.sleep(0.2)

    ## FUNCTIONAL test of read logs
    LOG_READ_QUERY = "select sensor_id, time, measure from sensor_log where sensor_id = (?)"
    with sqlite3.connect(DATASOURCE) as con:
        cur = con.execute(LOG_READ_QUERY, [69])
        rows = cur.fetchall()
        results = {}
        for i, row in enumerate(rows):
            results[i] = {"sensor_id":row[0], "time":row[1], "measure":row[2]}
        print(results)

    # ## API TEST of log retrieval
    print("Log retrieval")
    payload = {"sensor_id":69}
    r = requests.get(URL+"/log", params=payload)
    print(r.json())
  
    ## Functional test of the db
    SENSORS_READ_QUERY = "select * from sensors"
    with sqlite3.connect(DATASOURCE) as con:
        cur = con.execute(SENSORS_READ_QUERY)
        print(cur.fetchall())

    ## API test of get all sensors
    print("Test get all sensors")
    r = requests.get(URL+"/sensor")
    print(r.json())

    ## API test of update sensor
    print("update sensor")
    payload = {"sensor_id":69, "status":"99"}
    r = requests.put(URL+"/sensor", params=payload)
    print(r.json())
    # with sqlite3.connect(DATASOURCE) as con:
    #     con.execute("update sensors set status = 1 where sensor_id = 69")
    time.sleep(2)
    r = requests.get(URL+"/sensor", params={"sensor_id":69})
    print(r.json())

    ## API Test of not finding a sensor
    payload = {"sensor_id":-1}
    r = requests.get(URL+"/sensor", params=payload)
    print(r.json())

    ## API Test of delete
    for id in [69,71]:
        payload = {"sensor_id":id}
        r = requests.delete(URL+"/sensor", params=payload)
        print(r.json())

    pass