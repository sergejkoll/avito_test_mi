import uvicorn
from fastapi import FastAPI
from app.models.database import database
from app.routers import announcement
from app.crawler import work_with_crawler

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(announcement.router)
work_with_crawler.start_crawler()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
