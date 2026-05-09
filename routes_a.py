from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import Optional

from database import get_session
from models_a import Zivotinja, ZivotinjaCreate, ZivotinjaUpdate 

router = APIRouter(prefix="/resursi_a", tags=["Resurs A"])
