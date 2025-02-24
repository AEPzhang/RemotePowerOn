from fastapi import FastAPI
from config import POWER_ON, RUN_PORT  # 导入配置文件中的POWER_ON

app = FastAPI()

@app.get("/")
async def root():
    return {"code": "404"}

# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}

@app.get("/PowerOn")
async def power_on(formal: bool = POWER_ON):  # 使用配置文件中的默认值
    if formal:
        return {"code": "200", "PowerOn": True}
    else:
        return {"code": "200", "PowerOn": False}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=RUN_PORT)