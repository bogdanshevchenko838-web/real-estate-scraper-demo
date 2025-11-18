import json
from dataclasses import asdict
from typing import Iterable

import psycopg2

from .config import get_postgres_config
from .models import Property


def save_to_json(properties: Iterable[Property], path: str) -> None:
    data = [asdict(p) for p in properties]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def save_to_postgres(properties: Iterable[Property]) -> None:
    cfg = get_postgres_config()
    if cfg is None:
        raise RuntimeError("PostgreSQL config is missing")

    conn = psycopg2.connect(
        host=cfg.host,
        port=cfg.port,
        dbname=cfg.dbname,
        user=cfg.user,
        password=cfg.password,
    )
    conn.autocommit = True

    create_table_sql = """
    CREATE TABLE IF NOT EXISTS properties (
        id SERIAL PRIMARY KEY,
        title TEXT NOT NULL,
        price_usd INTEGER,
        address TEXT,
        beds INTEGER,
        baths REAL,
        area_sqft INTEGER,
        url TEXT
    );
    """

    insert_sql = """
    INSERT INTO properties (
        title, price_usd, address, beds, baths, area_sqft, url
    ) VALUES (%s, %s, %s, %s, %s, %s, %s);
    """

    try:
        with conn.cursor() as cur:
            cur.execute(create_table_sql)
            for p in properties:
                cur.execute(
                    insert_sql,
                    (
                        p.title,
                        p.price_usd,
                        p.address,
                        p.beds,
                        p.baths,
                        p.area_sqft,
                        p.url,
                    ),
                )
    finally:
        conn.close()
