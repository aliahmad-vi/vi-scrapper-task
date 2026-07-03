"""Fetches recent post titles from r/programming.

Reddit exposes a JSON version of every page by appending .json to the
URL, so no HTML parsing is needed here.
"""

from src.http_client import fetch_json
from src.models import Headline

REDDIT_URL = "https://www.reddit.com/r/programming.json?limit=25"


def get_headlines() -> list[Headline]:
    """Return headlines from the front page of r/programming."""
    data = fetch_json(REDDIT_URL)
    posts = data.get("data", {}).get("children", [])

    headlines = []
    for post in posts:
        post_data = post.get("data", {})
        title = post_data.get("title")
        permalink = post_data.get("permalink", "")

        if title:
            url = f"https://reddit.com{permalink}" if permalink else ""
            headlines.append(Headline(title, "Reddit r/programming", url))

    return headlines
