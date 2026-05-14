[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wxDq4rbD)
# Zadaća 2 - REST API aplikacija


## Opis domene

Domena: Informacioni sistem za upravljanje Zoo vrtom sa fokusom na životinje i njihove zabavne nastupe.

Svrha aplikacije: Ova REST API aplikacija služi kao centralizovani sistem za evidenciju dresiranih životinja i organizaciju njihovih javnih nastupa. Sistem je dizajniran da olakša rad dreserima i upravi Zoo vrta kroz digitalno praćenje ključnih podataka:

Evidencija životinja: Praćenje osnovnih informacija o životinjama (vrsta, starost, težina), njihovog zdravstvenog stanja i statusa dresure.

Upravljanje nastupima: Planiranje i organizacija nastupa, praćenje termina, opremljenosti i popularnosti (ocjena) svake izvedbe.

Cilj projekta: Primarni cilj je omogućiti potpunu CRUD funkcionalnost (kreiranje, čitanje, ažuriranje i brisanje) nad resursima životinja i nastupa, uz napredno filtriranje podataka radi bržeg pristupa informacijama (npr. pretraga po broju kaveza ili ocjeni publike).



## Entiteti

### Životinja 

| Naziv polja        | Tip podatka  | Napomena                    |
|--------------------|--------------|-----------------------------|
| id_zivotinje       | int          | Primary Key, auto-increment |
| ime_zivotinje      | str          | Obavezno polje              |
| vrsta_zivotinje    | str          | Obavezno polje              |
| starost            | int          | Obavezno polje              |
| tezina             | float        | Obavezno polje              |
| je_dresirana       | bool         | Obavezno polje              |
| opis               | Optional[str]| Nije obavezno               |
| broj_kaveza        | int          | Obavezno polje              |
| zdravstveni_karton | Optional[str]| Nije obavezno               |



### Dreserski nastup 

| Naziv polja        | Tip podatka  | Napomena                       |
|--------------------|--------------|--------------------------------|
| id_nastupa         | int          | Primary Key, auto-increment    |
| naziv              | str          | Obavezno polje                 |
| tezina_izvedbe     | int          | Skala od 1 do 5,obavezno polje |
| opis               | Optional[str]| Nije obavezno                  |
| potrebna_oprema    | bool         | Obavezno polje                 |
| vrijeme_pocetka    | Optional[str]| Format: "HH:MM", nije obavezno |
| ocjena_publike     | float        | Obavezno polje                 |
| max_broj_gledalaca | int          | Obavezno polje                 |
| id_zivotinje       | int          | Foreign Key, obavezno polje    |

## Tim

- **Student A**: Amel Tokić - resurs: `/zivotinja`
- **Student B**: Lejla Kadušić - resurs: `/performances` 

## Instalacija i pokretanje

### Preduvjeti

- Python 3.10 ili noviji
- pip

### Koraci

1. Klonirajte repozitorij:
```bash
git clone <url-repozitorija>
cd <naziv-repozitorija>
```

2. Kreirajte virtuelno okruženje:
```bash
python -m venv venv
```

3. Aktivirajte virtuelno okruženje:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

4. Instalirajte zavisnosti:
```bash
pip install -r requirements.txt
```

5. Pokrenite aplikaciju:
```bash
uvicorn main:app --reload
```

6. Otvorite browser na adresi: `http://localhost:8000/docs`

## API Endpointi

### Resurs A: `/zivotinja`

| Metoda | Ruta | Opis |
|--------|------|------|
| GET | `/zivotinja` | Lista svih životinja (query filteri: `vrsta_zivotinje`, `je_dresirana`) |
| GET | `/zivotinja/{id}` | Dohvatanje životinje po ID-u |
| POST | `/zivotinja` | Kreiranje nove životinje |
| PUT | `/zivotinja/{id}` | Potpuna zamjena životinje |
| PATCH | `/zivotinja/{id}` | Djelimično ažuriranje životinje |
| DELETE | `/zivotinja/{id}` | Brisanje životinje |




**Primjer zahtjeva:**
```bash
# Kreiranje nove zivotinje
curl -X POST "http://localhost:8000/zivotinja" \
  -H "Content-Type: application/json" \
  -d '{"ime_zivotinje": "Leo", "vrsta_zivotinje": "lav", "starost": 5, "tezina": 190.5, "je_dresirana": true, "broj_kaveza": 3}'

# Dohvatanje svih dresiranih lavova
curl "http://localhost:8000/zivotinja?vrsta_zivotinje=lav&je_dresirana=true"

# Djelimično azuriranje (samo starost)
curl -X PATCH "http://localhost:8000/zivotinja/1" \
  -H "Content-Type: application/json" \
  -d '{"starost": 6}'

```


### Resurs B: `/performances` 

| Metoda | Ruta | Opis |
| :--- | :--- | :--- |
| **GET** | `/performances` | Lista svih nastupa (opcionalni query filter: `min_rating`) |
| **GET** | `/performances/{id}` | Dohvatanje detalja jednog nastupa po ID-u |
| **POST** | `/performances` | Kreiranje novog nastupa (Status: **201 Created**) |
| **PUT** | `/performances/{id}` | Potpuna zamjena podataka postojećeg nastupa |
| **PATCH** | `/performances/{id}` | Djelimično ažuriranje podataka (koristi `exclude_unset=True`) |
| **DELETE** | `/performances/{id}` | Brisanje nastupa iz baze (Status: **204 No Content**) |

**Primjer zahtjeva:**
```bash
# Kreiranje novog nastupa
curl -X POST "http://localhost:8000/performances" \
  -H "Content-Type: application/json" \
  -d '{"title": "Nebeski letaci", "difficulty": 5, "description": "Akrobacije na visini", "required_equipment": true, "start_time": "20:30", "audience_rating": 4.9, "max_viewers": 300, "animal_id": 1}'

# Dohvatanje nastupa sa ocjenom vecom ili jednakom 4.0
curl "http://localhost:8000/performances?min_rating=4.0"

# Djelimično ažuriranje (samo broj gledalaca)
curl -X PATCH "http://localhost:8000/performances/1" \
  -H "Content-Type: application/json" \
  -d '{"max_viewers": 350}'
```

## Korištenje AI alata

>### Student A - Amel Tokić
>
>### Alat: Claude (Anthropic)
>**Model:** Claude Sonnet
>
>**Primjer 1:**
>- **Prompt:** "Kreiraj SQLModel klase za entitet Zivotinja sa poljima ime, vrsta, starost, tezina, je_dresirana, broj_kaveza, opis i zdravstveni_karton."
>- **Kako je pomoglo:** Generisao je osnovnu strukturu klase 'Zivotinja' sa ispravnim tipovima i Optional poljima.
>- **Prilagodbe:** Dodane su validacije polja u glavnoj tabeli (npr. `ge=0` za starost, `gt=0.0` za težinu, `ge=1` za broj_kaveza) i opisi polja putem `description` parametra.
>
>**Primjer 2:**
>- **Prompt:** "Implementiraj FastAPI PATCH endpoint koji koristi exclude_unset=True za djelimično ažuriranje SQLModel entiteta"
>- **Kako je pomoglo:** Generisao je ispravan PATCH endpoint i petljom koja postavlja samo proslijeđena polja.
>- **Prilagodbe:** Prilagođeno imenovanje varijabli prema domeni (zivotinja, id_zivotinje). Također, dodan HTTP 404 odgovor ukoliko entitet nije pronađen.

>### Student B - Lejla Kadušić
>
>### Alat: Gemini (Google)
>**Model:** Gemini 1.5 Flash
>
>**Primjer 1:**
>- **Prompt:** "Kreiraj SQLModel modele za entitet Performance koji uključuje naslov, težinu, opis, potrebnu opremu, vrijeme početka, ocjenu publike i maksimalan broj gledalaca. Poveži ga sa tabelom životinja preko animal_id."
>- **Kako je pomoglo:** Generisao je tri odvojena modela (Performance, PerformanceCreate, PerformanceUpdate) što je omogućilo čistu validaciju podataka i ispravno definisanje stranog ključa.
>- **Prilagodbe:** Promijenjeni su tipovi podataka (npr. audience_rating u float) i dodane su Optional oznake za PATCH model kako bi se omogućilo djelimično ažuriranje.
>
>**Primjer 2:**
>- **Prompt:** "Kako implementirati GET listu sa query parametrom za filtriranje po ocjeni u FastAPI koristeći SQLModel?"
>- **Kako je pomoglo:** Pružio je ispravnu sintaksu za select upite sa .where() klauzulom i pokazao kako se koristi Optional query parametar u funkciji.
>- **Prilagodbe:** Filter je postavljen na min_rating (veće ili jednako), čime je ispunjen uslov zadatka za postojanje najmanje jednog query parametra za filtriranje.


## Napomene

Integritet baze podataka: 

Aplikacija koristi relacioni model gdje su resursi Životinja i Nastup povezani putem stranog ključa (id_zivotinje). 
Ovo osigurava da svaki nastup mora biti dodijeljen postojećoj životinji, čime se sprječava unos nevažećih podataka.

## Provjera zadaće  2

### 1. Opis dodanog u Z1 i Z2

U `PerformanceCreate` model dodani Pydantic validatori. Blokiraju prazan string za `title`  i ograničavaju `difficulty` na opseg od 1 do 5. Ako podaci ne valjaju, baca se HTTP 422.
U `POST /performances/` endpoint dodan upit koji provjerava da li u bazi već postoji predstava sa istim `title`. Ako postoji, ruter baca HTTP 409 Conflict.
Napravljen novi `GET /performances/count` endpoint. Koristi `func.count(Performance.id)` da direktno iz baze izvuče ukupan broj redova i vrati ga kao JSON. Ruta je stavljena iznad `/{id` rute da je FastAPI ne bi pobrkao sa ID-jem.


### 2. Primjer zahtjeva i očekivanog odgovora za nove endpointe

POST /performances/
```json
{
  "title": "Lavlji šou",
  "difficulty": 3,
  "description": "Predstava sa lavovima",
  "required_equipment": true,
  "start_time": "18:00",
  "audience_rating": 4.7,
  "max_viewers": 200,
  "animal_id": 1
}
```

### Validatori i namjena
`title_ne_smije_biti_prazan`**: Određen za polje `title`. Provjerava da naziv predstave nije prazan string ili ispunjen samo razmacima.
`difficulty_mora_biti_u_opsegu`**: Određen za polje `difficulty`. Ograničava unos težine predstave isključivo na raspon od 1 do 5.

### 4. Greške i HTTP statusi
Prazan naslov / pogrešan broj (1-5): Vraća **HTTP 422** (Greška validacije).
Isti naslov na POST ruti: Vraća **HTTP 409** (Duplikat).
Nepostojeći ID u bazi: Vraća **HTTP 404** (Nije pronađeno).