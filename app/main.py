import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import APIKeyHeader

from .routers import router
from .database.session import  engine
from .database.models import Base
from .config import SERVICE_API_KEY

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

    await engine.dispose()



api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


async def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != SERVICE_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key"
        )


app = FastAPI(lifespan=lifespan,
              dependencies=[Depends(verify_api_key)])


app.include_router(router)


@app.get("/ping")
async def ping():
    return {"Are we suitable for each other?": "Uniquely!!!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)