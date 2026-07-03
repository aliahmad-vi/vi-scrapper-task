"""Filters a list of Headline objects down to ones matching given keywords."""

from src.models import Headline


def headline_matches(headline: Headline, keywords: list[str]) -> bool:
    """Return True if any keyword appears in the headline title (case-insensitive)."""
    title_lower = headline.title.lower()
    return any(keyword.lower() in title_lower for keyword in keywords)


def filter_headlines(headlines: list[Headline], keywords: list[str]) -> list[Headline]:
    """Return only the headlines that match at least one keyword."""
    return [h for h in headlines if headline_matches(h, keywords)]
