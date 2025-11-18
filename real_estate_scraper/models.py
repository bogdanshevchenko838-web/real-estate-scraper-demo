from dataclasses import dataclass
from typing import Optional


@dataclass
class Property:
    """Normalized representation of a real-estate listing."""

    title: str
    price_usd: Optional[int]
    address: str | None
    beds: Optional[int]
    baths: Optional[float]
    area_sqft: Optional[int]
    url: str | None
