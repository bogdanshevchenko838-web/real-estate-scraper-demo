import os
from typing import List

from bs4 import BeautifulSoup

from .models import Property
from .utils import parse_int, parse_float, parse_price_usd


def fetch_html(path: str) -> str:
    """
    Load local HTML file and return its content.
    For this demo, we always work with a local file (sample_page.html).
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"HTML file not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def parse_properties(html: str) -> List[Property]:
    """
    Parse property listings from the HTML structure used in sample_page.html.

    Expected structure:

    <div class="property-card">
        <a class="property-link" href="...">
            <h2 class="property-title">Title</h2>
        </a>
        <div class="property-price">$1,200</div>
        <div class="property-address">123 Main St, Sample City</div>
        <div class="property-meta">
            <span class="property-beds">2 beds</span>
            <span class="property-baths">1.5 baths</span>
            <span class="property-area">750 sqft</span>
        </div>
    </div>
    """
    soup = BeautifulSoup(html, "html.parser")
    cards = soup.select(".property-card")
    results: List[Property] = []

    for card in cards:
        # Title
        title_el = card.select_one(".property-title")
        title = title_el.get_text(strip=True) if title_el else ""

        # Link
        link_el = card.select_one(".property-link")
        url = link_el["href"] if link_el and link_el.has_attr("href") else ""

        # Price
        price_el = card.select_one(".property-price")
        price_text = price_el.get_text(strip=True) if price_el else None
        price_usd = parse_price_usd(price_text)

        # Address
        addr_el = card.select_one(".property-address")
        address = addr_el.get_text(strip=True) if addr_el else ""

        # Meta: beds, baths, area
        beds_el = card.select_one(".property-beds")
        baths_el = card.select_one(".property-baths")
        area_el = card.select_one(".property-area")

        beds = parse_int(beds_el.get_text(strip=True) if beds_el else None)
        baths = parse_float(baths_el.get_text(strip=True) if baths_el else None)
        area_sqft = parse_int(area_el.get_text(strip=True) if area_el else None)

        results.append(
            Property(
                title=title,
                price_usd=price_usd,
                address=address,
                beds=beds,
                baths=baths,
                area_sqft=area_sqft,
                url=url,
            )
        )

    return results
