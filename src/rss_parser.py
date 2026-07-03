"""Shared helper for parsing RSS feeds (used by Guardian and NYT sources).

RSS is just XML, so Python's built-in xml.etree.ElementTree is enough -
no external XML or feed-parsing library needed.
"""

import xml.etree.ElementTree as ET

from src.http_client import fetch_text
from src.models import Headline
from src.exceptions import FetchError


def parse_rss_titles(feed_url: str, source_name: str) -> list[Headline]:
    """Fetch an RSS feed and return one Headline per <item>."""
    raw_xml = fetch_text(feed_url)

    try:
        root = ET.fromstring(raw_xml)
    except ET.ParseError as err:
        raise FetchError(f"Could not parse RSS feed from {feed_url}: {err}") from err

    headlines = []
    for item in root.findall("./channel/item"):
        title_element = item.find("title")
        link_element = item.find("link")

        title = title_element.text if title_element is not None else None
        link = link_element.text if link_element is not None else ""

        if title:
            headlines.append(Headline(title.strip(), source_name, link or ""))

    return headlines
