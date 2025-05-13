from fastapi import FastAPI
import uvicorn
from routers.check_db import db_router
from core.config import settings
from routers.auth import auth_router
from routers.users import user_router

app = FastAPI()
app.include_router(db_router)
app.include_router(auth_router)
app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run('main:app', host=settings.HOST, port=settings.PORT, reload=settings.RELOAD)
