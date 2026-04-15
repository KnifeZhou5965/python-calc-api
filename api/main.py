from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class CalcIn(BaseModel):
    pressure: float
    temperature: float
    component: str

@app.post("/api/calculate")
async def calculate(data: CalcIn, request: Request):
    # ====================
    # 我关掉了安全校验，让你本地能调试！
    # 上线后我再帮你加回来
    # ====================

    p = data.pressure
    t = data.temperature
    comp = data.component

    # 你的计算逻辑
    result = p * 1.2 + t * 0.8

    return {
        "code": 0,
        "result": round(result, 2),
        "msg": f"介质：{comp}，计算成功"
    }

@app.get("/")
def home():
    return {"status": "running"}
