from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import Optional

from database import get_session
from models_a import Zivotinja, ZivotinjaCreate, ZivotinjaUpdate 

router = APIRouter(prefix="/resursi_a", tags=["Resurs A"])


# Dohvatanje liste svih životinja s opcionalnim filterima po vrsti i dresiranosti

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


# Dohvatanje jedne zivotinje po ID-u

@router.get("/{id_zivotinje}", response_model=Zivotinja)
def get_zivotinja(id_zivotinje: int, session: Session = Depends(get_session)):
    """
    Dohvata jednu životinju na osnovu njenog ID-a.
    Vraća HTTP 404 ukoliko životinja nije pronađena.
    """
    zivotinja = session.get(Zivotinja, id_zivotinje)
 
    if not zivotinja:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Životinja sa ID-em {id_zivotinje} nije pronađena."
        )
    return zivotinja


# Kreiranje nove zivotinje

@router.post("/", response_model=Zivotinja, status_code=status.HTTP_201_CREATED)
def create_zivotinja(zivotinja_data: ZivotinjaCreate, session: Session = Depends(get_session)):
   
    nova_zivotinja = Zivotinja.model_validate(zivotinja_data)
 
    session.add(nova_zivotinja)
    session.commit()
    session.refresh(nova_zivotinja)
    return nova_zivotinja