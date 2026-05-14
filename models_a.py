from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import field_validator

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

    @field_validator("ime_zivotinje")
    @classmethod
    def ime_ne_smije_biti_prazno(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Ime životinje ne smije biti prazno ili sadržavati samo razmake.")
        if len(v) < 2:
            raise ValueError("Ime životinje mora imati najmanje 2 karaktera.")
        return v
 
    @field_validator("vrsta_zivotinje")
    @classmethod
    def vrsta_ne_smije_biti_prazna(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Vrsta životinje ne smije biti prazna ili sadržavati samo razmake.")
        if len(v) < 3:
            raise ValueError("Vrsta životinje mora imati najmanje 3 karaktera.")
        return v
 
    @field_validator("starost")
    @classmethod
    def starost_mora_biti_pozitivna(cls, v: int) -> int:
        if v < 0:
            raise ValueError("Starost životinje ne može biti negativna.")
        if v > 150:
            raise ValueError("Starost životinje ne može biti veća od 150 godina.")
        return v
 
    @field_validator("tezina")
    @classmethod
    def tezina_mora_biti_pozitivna(cls, v: float) -> float:
        if v <= 0:
            raise ValueError("Težina životinje mora biti veća od 0 kg.")
        if v > 200_000:
            raise ValueError("Težina životinje ne može biti veća od 200 000 kg.")
        return v
 
    @field_validator("broj_kaveza")
    @classmethod
    def broj_kaveza_mora_biti_pozitivan(cls, v: int) -> int:
        if v < 1:
            raise ValueError("Broj kaveza mora biti pozitivan cijeli broj (minimalno 1).")
        return v


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

