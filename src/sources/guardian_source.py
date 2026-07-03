"""Fetches headlines from the Guardian's Technology RSS feed."""

from src.rss_parser import parse_rss_titles
from src.models import Headline

GUARDIAN_TECH_RSS = "https://www.theguardian.com/uk/technology/rss"


def get_headlines() -> list[Headline]:
    """Return headlines from the Guardian's Technology section."""
    return parse_rss_titles(GUARDIAN_TECH_RSS, "Guardian Technology")
