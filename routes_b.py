from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List, Optional

from database import get_session
from models_b import Performance, PerformanceCreate, PerformanceUpdate 

router = APIRouter(prefix="/performances", tags=["Performances"])


@router.post("/", status_code=201)
def create_performance(performance_data: PerformanceCreate, session: Session = Depends(get_session)):

    new_performance = Performance.from_orm(performance_data)
    session.add(new_performance)
    session.commit()
    session.refresh(new_performance)
    return new_performance

