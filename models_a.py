from sqlmodel import SQLModel, Field
from typing import Optional

class Zivotinja (SQLModel, table=True):
    ID_zivotinje: Optional[int] = Field(default=None, primary_key=True)

    ime_zivotinje : str = Field (min_length=1, description="Ime zivotinje.")
    vrsta_zivotinje : str = Field (min_length=1, description="Vrsta zivotinje.")
    starost: int = Field(ge=0, description="Starost životinje u godinama")
    tezina: float = Field(gt=0.0, description="Težina životinje u kilogramima")
    je_dresirana: bool = Field(description="Da li je životinja dresirana")
    broj_kaveza: int = Field(ge=1, description="Broj kaveza u kojem životinja boravi")
    opis: Optional[str] = Field(default=None, description="Dodatni opis životinje")
    zdravstveni_karton: Optional[str] = Field(default=None, description="Bilješke iz zdravstvenog kartona")


# Shema za kreiranje nove zivotinje bez ID-a

class ZivotinjaCreate(SQLModel):
    ime_zivotinje : str 
    vrsta_zivotinje : str
    starost : int
    tezina : float
    je_dresirana : bool
    broj_kaveza : int
    opis : Optional[str] = None
    zdravstveni_karton : Optional[str] = None


# Shema za djelimicno azuriranje


class ZivotinjaUpdate(SQLModel):
    ime_zivotinje : Optional[str] = None
    vrsta_zivotinje : Optional[str] = None
    starost : Optional[int] = None
    tezina : Optional[float] = None
    je_dresirana : Optional[bool] = None
    broj_kaveza : Optional[int] = None
    opis : Optional[str] = None
    zdravstveni_karton : Optional[str] = None

