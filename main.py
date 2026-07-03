"""Entry point for the news headline scraper.

Run with keywords as command-line arguments, e.g.:
    python main.py python security ai

Or run with no arguments and it will prompt for keywords instead.
"""

import sys

from src.exceptions import FetchError
from src.keyword_filter import filter_headlines
from src.sources import reddit_source, hackernews_source, guardian_source, nyt_source

SOURCES = [
    ("Reddit r/programming", reddit_source),
    ("Hacker News", hackernews_source),
    ("Guardian Technology", guardian_source),
    ("NYT Technology", nyt_source),
]


def get_keywords() -> list[str]:
    """Read keywords from command-line args, or prompt if none were given."""
    if len(sys.argv) > 1:
        return sys.argv[1:]

    raw = input("Enter keywords (space separated): ")
    return raw.split()


def collect_all_headlines() -> list:
    """Pull headlines from every source, skipping any source that fails."""
    all_headlines = []

    for name, source_module in SOURCES:
        print(f"Fetching from {name}...")
        try:
            all_headlines.extend(source_module.get_headlines())
        except FetchError as err:
            print(f"  Skipped {name}: {err}")

    return all_headlines


def main() -> None:
    """Read keywords, fetch from every source, and print matching headlines."""
    keywords = get_keywords()
    if not keywords:
        print("No keywords given, nothing to search for.")
        return

    all_headlines = collect_all_headlines()
    matches = filter_headlines(all_headlines, keywords)

    print(f"\nFound {len(matches)} matching headline(s) for {keywords}:\n")
    for headline in matches:
        print(headline)


if __name__ == "__main__":
    main()
