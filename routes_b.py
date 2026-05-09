from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List, Optional

from database import get_session
from models_b import Performance, PerformanceCreate, PerformanceUpdate 

router = APIRouter(prefix="/performances", tags=["Performances"])


@router.get("/", response_model=List[Performance])
def get_all_performances(min_rating: Optional[float] = None, session: Session = Depends(get_session)):
    query = select(Performance)
    
    if min_rating is not None:
        query = query.where(Performance.audience_rating >= min_rating)
        
    return session.exec(query).all()


@router.post("/", status_code=201)
def create_performance(performance_data: PerformanceCreate, session: Session = Depends(get_session)):

    new_performance = Performance.from_orm(performance_data)
    session.add(new_performance)
    session.commit()
    session.refresh(new_performance)
    return new_performance


@router.get("/{id}", response_model=Performance)
def get_performance(id: int, session: Session = Depends(get_session)):
    performance = session.get(Performance, id)
    
    if not performance:
        raise HTTPException(status_code=404, detail="Performance not found")
    
    return performance


@router.delete("/{id}", status_code=204)
def delete_performance(id: int, session: Session = Depends(get_session)):

    performance = session.get(Performance, id)
    
    if not performance:
        raise HTTPException(status_code=404, detail="Performance not found")
    

    session.delete(performance)
    session.commit()
    
    return None

@router.put("/{id}", response_model=Performance)
def update_performance(id: int, performance_data: PerformanceCreate, session: Session = Depends(get_session)):
    performance = session.get(Performance, id)
    
    if not performance:
        raise HTTPException(status_code=404, detail="Performance not found")
    
    for key, value in performance_data.dict().items():
        setattr(performance, key, value)
        
    session.commit()
    session.refresh(performance)
    return performance


@router.patch("/{id}", response_model=Performance)
def partial_update_performance(id: int, performance_data: PerformanceUpdate, session: Session = Depends(get_session)):
    performance = session.get(Performance, id)
    if not performance:
        raise HTTPException(status_code=404, detail="Performance not found")
    

    update_data = performance_data.dict(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(performance, key, value)
        
    session.commit()
    session.refresh(performance)
    return performance