[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wxDq4rbD)
# Zadaća 2 - REST API aplikacija

## O projektu

# Cirkus API

## Opis domene

Domena: Informacioni sistem za upravljanje Zoo vrtom sa fokusom na životinje i njihove zabavne nastupe.

Svrha aplikacije: Ova REST API aplikacija služi kao centralizovani sistem za evidenciju dresiranih životinja i organizaciju njihovih javnih nastupa. Sistem je dizajniran da olakša rad dreserima i upravi Zoo vrta kroz digitalno praćenje ključnih podataka:

Evidencija životinja: Praćenje osnovnih informacija o životinjama (vrsta, starost, težina), njihovog zdravstvenog stanja i statusa dresure.

Upravljanje nastupima: Planiranje i organizacija nastupa, praćenje termina, opremljenosti i popularnosti (ocjena) svake izvedbe.

Cilj projekta: Primarni cilj je omogućiti potpunu CRUD funkcionalnost (kreiranje, čitanje, ažuriranje i brisanje) nad resursima životinja i nastupa, uz napredno filtriranje podataka radi bržeg pristupa informacijama (npr. pretraga po broju kaveza ili ocjeni publike).

---

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

---

### Dreserski nastup 

| Naziv polja        | Tip podatka  | Napomena                       |
|--------------------|--------------|--------------------------------|
| id_nastupa         | int          | Primary Key, auto-increment    |
| naziv              | str          | Obavezno polje                 |
| tezina_izvedbe     | int          | Skala od 1 do 5                |
| opis               | Optional[str]| Nije obavezno                  |
| potrebna_oprema    | bool         | Obavezno polje                 |
| vrijeme_pocetka    | Optional[str]| Format: "HH:MM", nije obavezno |
| ocjena_publike     | float        | Obavezno polje                 |
| max_broj_gledalaca | int          | Obavezno polje                 |
| id_zivotinje       | int          | Foreign Key → Zivotinja        |

## Tim

- **Student A**: [Ime Prezime] - resurs: `/resursi_a`
- **Student B**: [Ime Prezime] - resurs: `/resursi_b`

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

### Resurs A: `/resursi_a`

| Metoda | Ruta | Opis |
|--------|------|------|
| GET | `/resursi_a` | Lista svih resursa (sa query filterom) |
| GET | `/resursi_a/{id}` | Dohvatanje resursa po ID-u |
| POST | `/resursi_a` | Kreiranje novog resursa |
| PUT | `/resursi_a/{id}` | Potpuna zamjena resursa |
| PATCH | `/resursi_a/{id}` | Djelimično ažuriranje resursa |
| DELETE | `/resursi_a/{id}` | Brisanje resursa |

**Primjer zahtjeva:**
```bash
# Kreiranje novog resursa
curl -X POST "http://localhost:8000/resursi_a" \
  -H "Content-Type: application/json" \
  -d '{"polje1": "vrijednost", "polje2": 123}'
```

### Resurs B: `/resursi_b`

[Analogno kao za Resurs A]

## Korištenje AI alata

### Alat: [GitHub Copilot / ChatGPT / ...]
**Model:** [GPT-4, Copilot model, ...]

**Primjer 1:**
- **Prompt:** [Npr. "Kreiraj SQLModel klasu za entitet Knjiga sa poljima naslov, autor, godina, isbn"]
- **Kako je pomoglo:** [Opis]
- **Prilagodbe:** [Da li ste morali prilagoditi generisani kod]

**Primjer 2:**
- **Prompt:** [Npr. "Implementiraj PATCH endpoint sa exclude_unset=True"]
- **Kako je pomoglo:** [Opis]
- **Prilagodbe:** [Opis]

## Napomene

[Dodatne napomene specifične za vašu implementaciju]