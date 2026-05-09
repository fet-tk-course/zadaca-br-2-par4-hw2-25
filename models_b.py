from sqlmodel import SQLModel, Field
from typing import Optional


class Performance(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str 
    difficulty: int 
    description: Optional[str] = None
    required_equipment: bool 
    start_time: Optional[str] = None 
    audience_rating: float 
    max_viewers: int 
    animal_id: int = Field(foreign_key="zivotinja.ID_zivotinje")

    

class PerformanceCreate(SQLModel):
title: str
difficulty: int
description: Optional[str] = None
required_equipment: bool
start_time: Optional[str] = None
audience_rating: float
max_viewers: int
animal_id: int

