from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from db.database import get_async_session
from fastapi.responses import JSONResponse

db_router = APIRouter()

db_router.get("/connect/")
async def check_connect(session: AsyncSession = Depends(get_async_session)):
    try:
        await session.execute(text("SELECT 1"))
        return JSONResponse({"status": "OK", "message": "Connected to database"})
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                           detail=f"Failed to connect to the database: {str(e)}")
