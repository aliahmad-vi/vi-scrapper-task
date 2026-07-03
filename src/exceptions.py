"""Custom exceptions for the news scraper."""


class FetchError(Exception):
    """Raised when a source cannot be reached or returns unexpected data."""
