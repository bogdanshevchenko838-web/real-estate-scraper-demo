import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

TARGET_URL = os.path.join(os.getcwd(), "sample_page.html")

@dataclass
class PostgresConfig:
    host: str
    port: int
    dbname: str
    user: str
    password: str

def get_postgres_config() -> PostgresConfig | None:
    host = os.getenv("PG_HOST")
    dbname = os.getenv("PG_DB")
    user = os.getenv("PG_USER")
    password = os.getenv("PG_PASSWORD")
    port = os.getenv("PG_PORT", "5432")

    if not all([host, dbname, user, password]):
        return None

    return PostgresConfig(
        host=host,
        port=int(port),
        dbname=dbname,
        user=user,
        password=password,
    )

