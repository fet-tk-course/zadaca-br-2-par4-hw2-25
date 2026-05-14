from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import field_validator


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


    @field_validator('title')
    @classmethod
    def title_ne_smije_biti_prazan(cls, v):
        if not v.strip():
            raise ValueError('Naziv predstave ne smije biti prazan string')
        return v.strip()

    @field_validator('difficulty')
    @classmethod
    def difficulty_mora_biti_u_opsegu(cls, v):
        if v < 1 or v > 5:
            raise ValueError('Težina (difficulty) mora biti broj između 1 i 5')
        return v



class PerformanceUpdate(SQLModel):
    title: Optional[str] = None
    difficulty: Optional[int] = None
    description: Optional[str] = None
    required_equipment: Optional[bool] = None
    start_time: Optional[str] = None
    audience_rating: Optional[float] = None
    max_viewers: Optional[int] = None
    animal_id: Optional[int] = None


    

