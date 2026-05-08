from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import Optional

from database import get_session
from models_a import Zivotinja, ZivotinjaCreate, ZivotinjaUpdate 

router = APIRouter(prefix="/resursi_a", tags=["Resurs A"])

# Dohvatanje liste svih zivotinja s opcionalnim filterima po vrsti i dresiranosti

@router.get("/", response_model=list[Zivotinja])
def get_all_zivotinje(
    vrsta_zivotinje: Optional[str] = None,
    je_dresirana: Optional[bool] = None,
    session: Session = Depends(get_session)
):
    query = select(Zivotinja)
 
    if vrsta_zivotinje is not None:
        query = query.where(Zivotinja.vrsta_zivotinje == vrsta_zivotinje)
    if je_dresirana is not None:
        query = query.where(Zivotinja.je_dresirana == je_dresirana)
 
    zivotinje = session.exec(query).all()
    return zivotinje