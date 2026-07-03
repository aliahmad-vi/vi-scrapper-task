"""Fetches top story titles from Hacker News.

Hacker News publishes an official public API (Firebase-backed) that
returns plain JSON, which is simpler and more reliable than parsing
the HTML page - and still uses no third-party libraries.
"""

from src.http_client import fetch_json
from src.models import Headline

TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

STORY_LIMIT = 25


def get_headlines() -> list[Headline]:
    """Return headlines for the current top stories on Hacker News."""
    story_ids = fetch_json(TOP_STORIES_URL)[:STORY_LIMIT]

    headlines = []
    for story_id in story_ids:
        item = fetch_json(ITEM_URL.format(story_id))
        title = item.get("title") if item else None

        if title:
            url = item.get("url", f"https://news.ycombinator.com/item?id={story_id}")
            headlines.append(Headline(title, "Hacker News", url))

    return headlines
