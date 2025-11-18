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
    try:
        save_to_postgres(properties)
        print("[+] Done: data inserted into PostgreSQL")
    except Exception as exc:
        print(f"[!] PostgreSQL not configured or not reachable: {exc}")


if __name__ == "__main__":
    main()
