from fastapi import FastAPI

# 创建一个FastAPI实例
app = FastAPI()

# 定义一个GET请求的路由，当访问根路径时，返回一个JSON对象
@app.get("/")
def read_root():
    return {"Hello": "FastAPI"}

# 定义一个GET请求的路由，当访问/items/{item_id}路径时，返回一个JSON对象，包含item_id和q参数
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# 定义一个POST请求的路由，当访问/items路径时，返回一个JSON对象，包含item_id和q参数
@app.post("/items/")
def create_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# 运行一个FastAPI应用
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
