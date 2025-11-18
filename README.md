# Real Estate Scraper Demo

Small demo project for a real-estate data pipeline:
- Scrapes property cards from an example listings page
- Normalizes data into a unified JSON schema
- Optionally stores data into a PostgreSQL table

> Selectors and target URL are placeholders and should be adjusted
> to the client's target websites.

## Tech stack

- Python 3.10+
- requests
- BeautifulSoup (bs4)
- PostgreSQL (via psycopg2)
- JSON export

## Project structure

- `main.py` – entry point, orchestrates the pipeline
- `real_estate_scraper/scraper.py` – HTTP client and HTML parser
- `real_estate_scraper/storage.py` – JSON and PostgreSQL persistence
- `real_estate_scraper/models.py` – dataclass for property records
- `real_estate_scraper/config.py` – basic configuration and env loading
- `real_estate_scraper/utils.py` – helpers for parsing numbers, prices, etc.

## Quick start

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
Run scraper and export to JSON
bash
python main.py
The script will:

Download the HTML from TARGET_URL (see config.py)

Parse property cards into a unified schema

Save data into sample_output.json

If PostgreSQL credentials are present – insert rows into the database.

Environment variables (optional, for PostgreSQL)
Create a .env file in the project root:

env

PG_HOST=localhost
PG_PORT=5432
PG_DB=real_estate
PG_USER=postgres
PG_PASSWORD=postgres
If .env is not provided, the script will skip PostgreSQL and only export JSON.

Notes
This repository is intended as a demo for:

Web scraping

Data normalization

JSON export

PostgreSQL integration

Selectors and database schema are easy to adapt for a real client project.

markdown

