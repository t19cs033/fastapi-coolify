from fastapi import FastAPI
import os

app = FastAPI(title="My FastAPI App")

@app.get("/")
def read_root():
    return {"message": "Hello World!", "status": "success"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Coolify用の設定
if __name__ == "__main__":
    import uvicorn
    PORT = int(os.environ.get("PORT", 8003))
    uvicorn.run("main:app", host="0.0.0.0", port=PORT)