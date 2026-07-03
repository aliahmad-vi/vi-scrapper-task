"""Small shared helpers for fetching data over HTTP.

Uses only Python's standard library (urllib, json) - no third-party
HTTP or parsing packages.
"""

import json
import urllib.request
import urllib.error

from src.exceptions import FetchError

# Some sites (Reddit especially) reject requests that don't look like
# they came from a real client with a clear identity, so we send a
# descriptive User-Agent following Reddit's own recommended format:
# "<platform>:<app name>:<version> (by /u/<username>)"
HEADERS = {"User-Agent": "windows:vital-interaction-headline-fetcher:1.0 (training script)"}

TIMEOUT_SECONDS = 10


def fetch_text(url: str) -> str:
    """Fetch a URL and return the raw response body as text."""
    request = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            return response.read().decode("utf-8", errors="replace")
    except (urllib.error.URLError, urllib.error.HTTPError) as err:
        raise FetchError(f"Could not fetch {url}: {err}") from err


def fetch_json(url: str):
    """Fetch a URL and parse the response body as JSON."""
    raw = fetch_text(url)
    try:
        return json.loads(raw)
    except json.JSONDecodeError as err:
        raise FetchError(f"Invalid JSON from {url}: {err}") from err
