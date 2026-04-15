from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class CalcIn(BaseModel):
    pressure: float
    temperature: float
    component: str

@app.post("/api/calculate")
async def calculate(data: CalcIn, request: Request):
    # 安全校验：只允许微信小程序调用
    referer = request.headers.get("referer", "")
    if "servicewechat.com" not in referer:
        return {"code": -1, "msg": "非法调用"}

    # 下面写你的 Python 计算逻辑
    p = data.pressure
    t = data.temperature
    comp = data.component

    # 示例计算，你可以替换成任意复杂公式
    result = p * 1.2 + t * 0.8

    return {
        "code": 0,
        "result": round(result, 2),
        "msg": f"计算成功，介质：{comp}"
    }

@app.get("/")
def home():
    return {"status": "running"}
