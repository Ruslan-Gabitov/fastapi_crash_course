from typing import Annotated
from fastapi import Depends, FastAPI
from contextlib import asynccontextmanager
from database import create_table, delete_tables
from schemas import STaskAdd
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_table()
    print("База готова")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
