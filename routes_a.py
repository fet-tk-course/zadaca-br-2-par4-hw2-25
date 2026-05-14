from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import Optional

from database import get_session
from models_a import Zivotinja, ZivotinjaCreate, ZivotinjaUpdate 

router = APIRouter(prefix="/zivotinja", tags=["Zivotinja"])


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


# Statistika životinja grupisana po vrsti
# Ruta /statistika mora biti PRIJE /{id_zivotinje} kako FastAPI ne bi
# pokušao interpretirati string "statistika" kao integer ID.
 
@router.get("/statistika", response_model=list[dict])
def get_statistika_po_vrsti(session: Session = Depends(get_session)):
   
    zivotinje = session.exec(select(Zivotinja)).all()
 
    if not zivotinje:
        return []
 
    grupe: dict[str, dict] = {}
    for z in zivotinje:
        vrsta = z.vrsta_zivotinje
        if vrsta not in grupe:
            grupe[vrsta] = {
                "vrsta_zivotinje": vrsta,
                "ukupno": 0,
                "ukupna_starost": 0,
                "ukupna_tezina": 0.0,
                "broj_dresiranih": 0,
            }
        grupe[vrsta]["ukupno"] += 1
        grupe[vrsta]["ukupna_starost"] += z.starost
        grupe[vrsta]["ukupna_tezina"] += z.tezina
        if z.je_dresirana:
            grupe[vrsta]["broj_dresiranih"] += 1
 
    rezultat = []
    for vrsta, podaci in grupe.items():
        n = podaci["ukupno"]
        rezultat.append({
            "vrsta_zivotinje":   vrsta,
            "ukupno":            n,
            "prosjecna_starost": round(podaci["ukupna_starost"] / n, 2),
            "prosjecna_tezina":  round(podaci["ukupna_tezina"]  / n, 2),
            "broj_dresiranih":   podaci["broj_dresiranih"],
        })
 
    rezultat.sort(key=lambda x: x["ukupno"], reverse=True)
    return rezultat

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

     ### HTTP 409 konflikt                -> ZADATAK 1
    postojeca = session.exec(
        select(Zivotinja).where(
            Zivotinja.ime_zivotinje == zivotinja_data.ime_zivotinje,
            Zivotinja.broj_kaveza == zivotinja_data.broj_kaveza
        )
    ).first()
 
    if postojeca:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                f"Životinja s imenom '{zivotinja_data.ime_zivotinje}' "
                f"već postoji u kavezu broj {zivotinja_data.broj_kaveza}."
            )
        )
   
    nova_zivotinja = Zivotinja.model_validate(zivotinja_data)
 
    session.add(nova_zivotinja)
    session.commit()
    session.refresh(nova_zivotinja)
    return nova_zivotinja


# Potpuna zamjena zivotinje

@router.put("/{id_zivotinje}", response_model=Zivotinja)
def update_zivotinja(
    id_zivotinje: int,
    zivotinja_data: ZivotinjaCreate,
    session: Session = Depends(get_session)
):
    zivotinja = session.get(Zivotinja, id_zivotinje)
 
    if not zivotinja:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Životinja sa ID-em {id_zivotinje} nije pronađena."
        )
 
    nova_data = zivotinja_data.model_dump()
    for key, value in nova_data.items():
        setattr(zivotinja, key, value)
 
    session.add(zivotinja)
    session.commit()
    session.refresh(zivotinja)
    return zivotinja


# Djelimicno azuriranje zivotinje

@router.patch("/{id_zivotinje}", response_model=Zivotinja)
def partial_update_zivotinja(
    id_zivotinje: int,
    zivotinja_data: ZivotinjaUpdate,
    session: Session = Depends(get_session)
):
    zivotinja = session.get(Zivotinja, id_zivotinje)
 
    if not zivotinja:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Životinja sa ID-em {id_zivotinje} nije pronađena."
        )
 
    azurirana_polja = zivotinja_data.model_dump(exclude_unset=True)
    for key, value in azurirana_polja.items():
        setattr(zivotinja, key, value)
 
    session.add(zivotinja)
    session.commit()
    session.refresh(zivotinja)
    return zivotinja


# Brisanje životinje

@router.delete("/{id_zivotinje}", status_code=status.HTTP_204_NO_CONTENT)
def delete_zivotinja(id_zivotinje: int, session: Session = Depends(get_session)):
    zivotinja = session.get(Zivotinja, id_zivotinje)
 
    if not zivotinja:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Životinja sa ID-em {id_zivotinje} nije pronađena."
        )
 
    session.delete(zivotinja)
    session.commit()