import re
from typing import Optional


def parse_int(value: str | None) -> Optional[int]:
    if not value:
        return None
    digits = re.findall(r"\d+", value.replace(",", ""))
    return int(digits[0]) if digits else None


def parse_float(value: str | None) -> Optional[float]:
    if not value:
        return None
    match = re.search(r"\d+(?:\.\d+)?", value.replace(",", "."))
    return float(match.group(0)) if match else None


def parse_price_usd(value: str | None) -> Optional[int]:
    """Extract numeric price from strings like '$1,234,000'."""
    if not value:
        return None
    cleaned = value.replace(",", "")
    match = re.search(r"\d+", cleaned)
    return int(match.group(0)) if match else None
