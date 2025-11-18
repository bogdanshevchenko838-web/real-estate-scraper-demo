from typing import List
import requests
from bs4 import BeautifulSoup

from .models import Property
from .utils import parse_int, parse_float, parse_price_usd


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/123.0 Safari/537.36"
    )
}


def fetch_html(url: str) -> str:
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    return resp.text


def parse_properties(html: str) -> List[Property]:
    """
    Parse property cards from HTML.

    This is a generic example. In a real project we adjust selectors
    to match the target website structure.

    Expected HTML structure:

    <div class="property-card">
        <a class="property-link" href="...">
            <h2 class="property-title">Nice 2BR Apartment</h2>
        </a>
        <div class="property-price">$1,200</div>
        <div class="property-address">123 Main St, City</div>
        <div class="property-beds">2 beds</div>
        <div class="property-baths">1.5 baths</div>
        <div class="property-area">750 sqft</div>
    </div>
    """
    soup = BeautifulSoup(html, "html.parser")
    cards = soup.select(".property-card")
    properties: List[Property] = []

    for card in cards:
        title_el = card.select_one(".property-title")
        price_el = card.select_one(".property-price")
        addr_el = card.select_one(".property-address")
        beds_el = card.select_one(".property-beds")
        baths_el = card.select_one(".property-baths")
        area_el = card.select_one(".property-area")
        link_el = card.select_one("a.property-link")

        title = title_el.get_text(strip=True) if title_el else "Untitled property"
        price = parse_price_usd(price_el.get_text(strip=True) if price_el else None)
        address = addr_el.get_text(strip=True) if addr_el else None
        beds = parse_int(beds_el.get_text(strip=True) if beds_el else None)
        baths = parse_float(baths_el.get_text(strip=True) if baths_el else None)
        area_sqft = parse_int(area_el.get_text(strip=True) if area_el else None)
        url = link_el["href"] if link_el and link_el.has_attr("href") else None

        properties.append(
            Property(
                title=title,
                price_usd=price,
                address=address,
                beds=beds,
                baths=baths,
                a
