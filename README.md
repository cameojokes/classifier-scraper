# Hit Factor Scraper

Work in progress. The "API"(really a SSR route) is rate limited so this is limited to one HF request. Increase at your own risk.

## Usage

Get the session id from a browser request cookie header to uspsa.org when logged in like: `Cookie: ...; session=[copy_this]; ...;`

```shell
pip3 install -r requirements.txt
export APP_SESSION_ID=[session_id]
python scrape.py | jq
```
