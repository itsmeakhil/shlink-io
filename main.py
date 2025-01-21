from fastapi import FastAPI
import uvicorn
from app.api import api as api_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}


app.include_router(api_router.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8090, reload=True)
