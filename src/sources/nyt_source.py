"""Fetches headlines from the New York Times Technology RSS feed."""

from src.rss_parser import parse_rss_titles
from src.models import Headline

NYT_TECH_RSS = "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"


def get_headlines() -> list[Headline]:
    """Return headlines from the NYT's Technology section."""
    return parse_rss_titles(NYT_TECH_RSS, "NYT Technology")
