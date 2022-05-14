import json
from flask import Flask, request, current_app

import datalayer.logs as logs
import datalayer.sensors

app = Flask(__name__)

@app.route("/")
def home():
    # return current_app.send_static_file("index.html")
    return "Hello"

@app.route("/sensor", methods=["GET","POST","PUT","DELETE"])
def sensor():
    if request.method == "GET":
        db_id = request.args.get("db_id")
        sensor_id = request.args.get("sensor_id")
        sensor = datalayer.sensors.get(sensor_id, db_id)
        result = json.dumps(sensor)
        return result
    
    if request.method == "POST":
        sensor_id = request.args.get("sensor_id")
        sens_name = request.args.get("name")
        sens_type = request.args.get("type")
        sens_status = request.args.get("status")
        db_id = datalayer.sensors.post(sensor_id, sens_name, sens_type, sens_status)
        result = json.dumps(db_id)
        return result

    if request.method == "DELETE":
        sensor_id = request.args.get("sensor_id")
        result = datalayer.sensors.delete(sensor_id)
        result = json.dumps(result)
        return result

    if request.method == "PUT":
        sensor_id = request.args.get("sensor_id")
        status = request.args.get("status")
        stats = str(status)
        result = datalayer.sensors.put(sensor_id, status)
        result = json.dumps(result)
        return result


@app.route("/log", methods=["GET","POST"])
def log():
    if request.method == "GET":
        sensor_id = request.args.get("sensor_id")
        log = logs.get(sensor_id)
        result = json.dumps(log)
        return result

    if request.method == "POST":
        sensor_id = request.args.get("sensor_id")
        time = request.args.get("time")
        measure = request.args.get("measure")
        log = logs.post(sensor_id, time, measure)
        result = json.dumps(log)
        return result


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)