from fastapi import FastAPI
from config import POWER_ON_DEFAULT  # 导入配置文件中的POWER_ON_DEFAULT

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/PowerOn")
async def power_on(name: str, formal: bool = POWER_ON_DEFAULT):  # 使用配置文件中的默认值
    if formal:
        return {"message": f"Greetings, {name}!"}
    else:
        return {"message": f"Hello, {name}!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)