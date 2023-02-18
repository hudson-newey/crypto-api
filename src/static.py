BASE_URL: str = "https://www.coingecko.com/en/coins/"
PRICE_RE = r"Bitcoin is USD \$[0-9,]*\.[0-9]*"
VOLUME_RE = r"volume of \$[0-9,]*"
CHANGE_RE = r"[\-0-9\.,]*\% in the last 24 hours"

INIT_MESSAGE = """
To use the crypto api, load the website 'http://localhost:5000?v=coin name' in your web browser
e.g. http://localhost:5000/?v=bitcoin
"""
