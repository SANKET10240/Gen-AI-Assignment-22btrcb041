from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..services.competitors import fetch_insights_with_competitors
from .deps import get_db

router = APIRouter()

@router.post("/fetch-insights-with-competitors")
async def competitor_insights(
    payload: dict,
    db: AsyncSession = Depends(get_db),
):
    # Simple passthrough; you can validate with Pydantic schema later
    result = await fetch_insights_with_competitors(payload, db)
    return result
