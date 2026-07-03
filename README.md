# News Headline Scraper

Week 1 - Python Task (Module 2, Part B)

A command-line script that takes keywords and prints matching headlines
(with their links) from four sources: Reddit (r/programming), Hacker
News, the Guardian (Technology), and the New York Times (Technology).

No third-party packages are used - only Python's standard library
(`urllib`, `json`, `xml.etree.ElementTree`).

## How each source is reached


| Reddit r/programming | JSON | Reddit's own `.json` endpoint |
| Hacker News | JSON | Official public Hacker News API (Firebase) |
| Guardian Technology | RSS (XML) | Public RSS feed, parsed with `xml.etree.ElementTree` |
| NYT Technology | RSS (XML) | Public RSS feed, parsed with `xml.etree.ElementTree` |

Hacker News is fetched through its official JSON API rather than by
scraping the HTML page - it's simpler, more reliable, and still needs
no external parsing library.

Reddit sends a descriptive User-Agent (following Reddit's recommended
format) to reduce the chance of being blocked. Reddit can still
occasionally block requests (403) depending on IP/rate limits - if
that happens the script skips it and continues with the other three
sources instead of crashing.

## Project structure

```
news-scraper/
├── main.py                       # entry point - reads keywords, runs everything
├── requirements.txt
├── src/
│   ├── models.py                  # Headline data class (prints title + link)
│   ├── exceptions.py               # FetchError
│   ├── http_client.py               # shared fetch_text / fetch_json helpers
│   ├── rss_parser.py                 # shared RSS parsing (used by Guardian + NYT)
│   ├── keyword_filter.py              # matching logic
│   └── sources/
│       ├── reddit_source.py
│       ├── hackernews_source.py
│       ├── guardian_source.py
│       └── nyt_source.py

```

## Setup (virtual environment)

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running the app

With keywords as arguments:
```bash
python main.py python security ai
```

Or with no arguments (it will prompt you):
```bash
python main.py
```

Each matching headline is printed with its source and link underneath,
so you can trace it back to the original page.

## Linting

```bash
pylint src/ main.py
```

Currently rated **10.00/10**.

## Note

This script needs an internet connection to fetch live headlines. If
any single source is down or blocks the request, that source is
skipped with a message - the script still shows results from the
others instead of crashing.
