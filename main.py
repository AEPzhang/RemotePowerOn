from fastapi import FastAPI
from config import POWER_STATE, RUN_PORT  # 导入配置文件中的POWER_ON

app = FastAPI()

@app.get("/")
async def root():
    return {"code": "404"}


@app.get("/PowerState")
async def power_on(formal: bool = POWER_STATE):  # 使用配置文件中的默认值
    if formal:
        return {"code": "200", "POWER_STATE": True}
    else:
        return {"code": "200", "POWER_STATE": False}

@app.get("/PowerSwitch")
async def power_switch():
    global POWER_STATE
    POWER_STATE = not POWER_STATE
    print("POWER_STATE:", POWER_STATE)
    return {"code": "200", "POWER_STATE": POWER_STATE}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=RUN_PORT)