#!/bin/bash
# --rm \

docker run -d \
    -p 5050:5050 \
    -it \
    --name iot-web \
    --mount type=bind,source="$(pwd)"/data,target=/data \
    --mount type=bind,source="$(pwd)"/app,target=/app   \
    iot-web:latest