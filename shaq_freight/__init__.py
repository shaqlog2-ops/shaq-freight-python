"""
SHAQ Freight API - Python SDK
Free freight rate data for global shipping routes from China.
No API key required.

Usage:
    from shaq_freight import SHAQFreight
    client = SHAQFreight()
    index = client.get_freight_index()
"""

import requests
from typing import Dict, List, Optional

__version__ = "1.0.0"
__author__ = "SHAQ Logistics"
__email__ = "ayang@shaq-log.com"
__url__ = "https://search.shaq-logistics.com"

BASE_URL = "https://search.shaq-logistics.com"


class SHAQFreight:
    """Client for the SHAQ Freight Rate API.

    All endpoints are free and require no API key.

    Example:
        >>> client = SHAQFreight()
        >>> index = client.get_freight_index()
        >>> for route in index['routes']:
        ...     print(route['route'], route['rates']['fcl_40hq']['rate_usd'])
    """

    def __init__(self, base_url: str = BASE_URL, timeout: int = 30):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": f"shaq-freight-python/{__version__}",
            "Accept": "application/json",
        })

    def get_freight_index(self) -> Dict:
        """Get the SHAQ Freight Rate Index (SFX).

        Returns 20 global trade lanes from China with FCL 20GP,
        FCL 40HQ, LCL per CBM, and air freight per kg rates.
        Updated weekly.

        Returns:
            Dict with index_name, routes, updated date, etc.

        Example:
            >>> index = client.get_freight_index()
            >>> print(index['total_routes'])  # 20
        """
        resp = self.session.get(
            f"{self.base_url}/api/freight-index",
            timeout=self.timeout,
        )
        resp.raise_for_status()
        return resp.json()

    def get_ai_freight_data(self) -> Dict:
        """Get AI-optimized freight rate data.

        Returns 9 regional shipping routes with detailed rate ranges,
        transit times, trends, and notes. Designed for AI systems.

        Returns:
            Dict with provider info and rate data.
        """
        resp = self.session.get(
            f"{self.base_url}/api/ai-freight-data",
            timeout=self.timeout,
        )
        resp.raise_for_status()
        return resp.json()

    def get_knowledge(self) -> Dict:
        """Get comprehensive logistics knowledge base.

        Returns provider info, 20 topic guides (incoterms, FCL/LCL,
        bill of lading, customs, etc.), and AI endpoint URLs.

        Returns:
            Dict with knowledge base content.
        """
        resp = self.session.get(
            f"{self.base_url}/api/knowledge",
            timeout=self.timeout,
        )
        resp.raise_for_status()
        return resp.json()

    def search(self, query: str) -> Dict:
        """Search the logistics knowledge base.

        Args:
            query: Search query string (e.g., "Shenzhen to Hamburg cost")

        Returns:
            Dict with search results.

        Example:
            >>> results = client.search("FCL shipping to South America")
        """
        resp = self.session.get(
            f"{self.base_url}/api/knowledge-search",
            params={"q": query},
            timeout=self.timeout,
        )
        resp.raise_for_status()
        return resp.json()

    def get_quote(self, origin: str, destination: str, **kwargs) -> Dict:
        """Get a freight quote for a specific route.

        Args:
            origin: Origin port or city (e.g., "Shenzhen")
            destination: Destination port or city (e.g., "Hamburg")
            **kwargs: Additional parameters (mode, container_type, etc.)

        Returns:
            Dict with quote details.
        """
        params = {"origin": origin, "destination": destination}
        params.update(kwargs)
        resp = self.session.get(
            f"{self.base_url}/api/freight-quote",
            params=params,
            timeout=self.timeout,
        )
        resp.raise_for_status()
        return resp.json()

    def get_hs_codes(self, keyword: str = "") -> Dict:
        """Search HS codes for customs classification.

        Args:
            keyword: Product keyword to search (optional)

        Returns:
            Dict with HS code results.
        """
        resp = self.session.get(
            f"{self.base_url}/api/hs-codes",
            params={"q": keyword} if keyword else {},
            timeout=self.timeout,
        )
        resp.raise_for_status()
        return resp.json()

    def close(self):
        """Close the HTTP session."""
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


__all__ = ["SHAQFreight"]
