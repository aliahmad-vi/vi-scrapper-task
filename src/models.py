"""Headline model - a single normalized result from any news source."""


class Headline:
    """Represents one headline pulled from a source, in a common shape."""

    def __init__(self, title: str, source: str, url: str = ""):
        self.title = title
        self.source = source
        self.url = url

    def __str__(self) -> str:
        base = f"[{self.source}] {self.title}"
        if self.url:
            return f"{base}\n    {self.url}"
        return base

    def __repr__(self) -> str:
        return f"Headline(title={self.title!r}, source={self.source!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Headline):
            return NotImplemented
        return self.title == other.title and self.source == other.source
