from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    pressure: float
    temperature: float
    component: str

@app.post("/api/calculate")
def calculate(item: Item):
    p = item.pressure
    t = item.temperature
    comp = item.component
    result = p * 1.2 + t * 0.8
    return {
        "code": 0,
        "result": round(result, 2),
        "msg": f"介质 {comp} 计算成功"
    }

@app.get("/")
def root():
    return {"status": "running"}
