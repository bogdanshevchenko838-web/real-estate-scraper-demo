# Real Estate Scraper Demo

A clean, minimal demo project showing how to build a real-estate data extraction pipeline using Python.  
The goal of this repository is to demonstrate skills in:

- Web scraping (requests + BeautifulSoup)
- Data normalization into a unified schema
- JSON export
- Optional PostgreSQL integration
- Clean code structure suitable for production

The project uses a mock/example page structure — selectors can be easily replaced with real client websites.

---

## Tech Stack

- **Python 3.10+**
- **requests** — HTTP client  
- **BeautifulSoup4** — HTML parsing  
- **psycopg2** — PostgreSQL driver  
- **python-dotenv** — environment variable loader  

---

## 📁 Project Structure
```
real-estate-scraper-demo/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── real_estate_scraper/
├── init.py
├── config.py # Loads TARGET_URL and PostgreSQL credentials
├── models.py # Dataclass for Property
├── scraper.py # HTML downloader + property parser
├── storage.py # JSON + PostgreSQL storage
└── utils.py # Helpers (parsing numbers, floats, prices)
```
---

## Quick Start

### 1. Create & activate virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Run the scraper
```bash
python main.py

The script will:
- Download HTML from TARGET_URL (located in config.py)
- Parse property cards into a normalized Python dataclass
- Save results into sample_output.json
- Insert rows into PostgreSQL (if configured)
```

## 3. PostgreSQL Integration (optional)
```bash
To enable database saving, create a .env file in the project root:
PG_HOST=localhost
PG_PORT=5432
PG_DB=real_estate
PG_USER=postgres
PG_PASSWORD=postgres
If .env is missing, the script gracefully falls back to JSON-only mode.
```

## 📝 Example Output (JSON)

```json
[
  {
    "title": "Modern 2BR Apartment Downtown",
    "price_usd": 1200,
    "address": "123 Main St, Sample City",
    "beds": 2,
    "baths": 1.5,
    "area_sqft": 750,
    "url": "https://example.com/listing/123"
  }
]
```

## 📌 Notes
```
Selectors in scraper.py are placeholders meant to be adapted to real listings.
Useful as a starting point for real estate aggregation, rent-price analysis, or ETL pipelines.
The code is written to be clear, modular, and easy to extend.
```