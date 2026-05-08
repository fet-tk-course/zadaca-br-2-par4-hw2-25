from sqlmodel import SQLModel, Field
from typing import Optional

class Zivotinja (SQLModel, table=True):
    ID_zivotinje: Optional[int] = Field(default=None, primary_key=True)

    ime_zivotinje : str = Field (min_length=1, description="Ime zivotinje.")
    starost: int = Field(ge=0, description="Starost životinje u godinama")
    tezina: float = Field(gt=0.0, description="Težina životinje u kilogramima")
    je_dresirana: bool = Field(description="Da li je životinja dresirana")
    broj_kaveza: int = Field(ge=1, description="Broj kaveza u kojem životinja boravi")
    opis: Optional[str] = Field(default=None, description="Dodatni opis životinje")
    zdravstveni_karton: Optional[str] = Field(default=None, description="Bilješke iz zdravstvenog kartona")

