import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI

from .routers import router
from .database.session import  engine
from .database.models import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

    await engine.dispose()

app = FastAPI(lifespan=lifespan)


app.include_router(router)


@app.get("/ping")
async def ping():
    return {"Are we suitable for each other?": "Uniquely!!!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)