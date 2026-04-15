from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class CalcIn(BaseModel):
    pressure: float
    temperature: float
    component: str

@app.post("/api/calculate")
async def calculate(data: CalcIn, request: Request):
    referer = request.headers.get("referer", "")
    if "servicewechat.com" not in referer:
        return {"code": -1, "msg": "非法调用"}

    p = data.pressure
    t = data.temperature
    comp = data.component
    result = p * 1.2 + t * 0.8

    return {
        "code": 0,
        "result": round(result, 2),
        "msg": f"介质：{comp}，计算成功"
    }

@app.get("/")
def home():
    return {"status": "running"}
