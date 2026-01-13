import traceback

import psycopg2

from real_estate_scraper.config import TARGET_URL
from real_estate_scraper.scraper import fetch_html, parse_properties
from real_estate_scraper.storage import save_to_json, save_to_postgres


def main() -> None:
    print(f"[+] Fetching HTML from: {TARGET_URL}")
    html = fetch_html(TARGET_URL)

    print("[+] Parsing properties...")
    properties = parse_properties(html)
    print(f"[+] Parsed {len(properties)} properties")

    print("[+] Saving to sample_output.json")
    save_to_json(properties, "sample_output.json")

    print("[+] Trying to save to PostgreSQL (if configured)...")
    # save_to_postgres может выбросить RuntimeError при отсутствии конфигурации
    # и psycopg2.OperationalError при проблемах подключения/БД.
    try:
        save_to_postgres(properties)
        print("[+] Done: data inserted into PostgreSQL")
    except RuntimeError as exc:
        print(f"[!] PostgreSQL not configured: {exc}")
    except psycopg2.OperationalError as exc:
        print(f"[!] PostgreSQL connection/DB error: {exc}")
    except Exception as exc:
        print(f"[!] Unexpected PostgreSQL error (not configuration): {exc}")
        traceback.print_exc()
        raise


if __name__ == "__main__":
    main()
