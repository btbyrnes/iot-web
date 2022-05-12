import json
import logging
from flask import Flask, request, current_app

import datalayer.logs as logs
import datalayer.sensors

logging.basicConfig(format="%(asctime)s %(name)-12s %(funcName)-12s %(levelname)-8s %(message)s", datefmt="%m-%d %H:%M", filename="app/app.log", filemode="w")

app = Flask(__name__)

@app.route("/")
def home():
    # return current_app.send_static_file("index.html")
    return "Hello"

@app.route("/sensor", methods=["GET","POST"])
def sensor():
    if request.method == "GET":
        logging.debug(request.args)
        db_id = request.args.get("db_id")
        sensor_id = request.args.get("sensor_id")
        sensor = datalayer.sensors.get_sensor(sensor_id, db_id)

        result = json.dumps(sensor)
        logging.debug(result)
        return result
    
    if request.method == "POST":
        sensor_id = request.args.get("sensor_id")
        sens_name = request.args.get("name")
        sens_type = request.args.get("type")

        db_id = datalayer.sensors.post_sensor(sensor_id, sens_name, sens_type)
        result = json.dumps(db_id)
        logging.debug(result)
        return result


@app.route("/sensors", methods=["GET"])
def sensors():
    if request.method == "GET":
        sensors = datalayer.sensors.get_sensor(sensor_id=None, db_id=None)
        return json.dumps(sensors)

            

@app.route("/log", methods=["GET","POST"])
def log():
    if request.method == "GET":
        # logging.debug(request.args)
        db_id = request.args.get("db_id")
        log = logs.get_log(db_id)
        
        result = json.dumps(log)
        # logging.debug(str(result))
        return result

    if request.method == "POST":
        # logging.debug(str(request.args))
        db_id = request.args.get("db_id")
        sensor_id = request.args.get("sensor_id")
        time = request.args.get("time")
        measure = request.args.get("measure")

        log = logs.post_log(db_id, sensor_id, time, measure)
        result = json.dumps(log)
        # logging.debug(str(result))
        return result


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)