# main.py
import random
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# data class
class Sensor(BaseModel):
    sensorID: str
    description: Optional[str] = None
    value: Optional[float] = None
    unit: str
    nominalValue: Optional[str] = None

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message" : "sample data api"}

# @app.post("/sensors/")
# async def ceate_sensor(sensor: Sensor):
#     sensor_dict = sensor.dict()
#     diff = math.abs(value - random.Random()*sensor.sensorID)
#     sensor.value = random.Random()*sensor.sensorID
#     sensor_dict.update({"diff" : diff})
#     return sensor_dict

@app.get("/sensor/{sensor_id}")
async def read_item(sensor_id: int):
    return {"sensor_id":update_value(sensor_id)}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

def update_value(id: int):
    deviation = 0
    for _ in range(id):
        deviation += (random.random() - 0.5)
    return id + deviation/id
