import requests
import pandas as pd
import io
from loguru import logger


class IEXScraper:
    def __init__(self):
        self.url = "https://www.iexindia.com/market-data/day-ahead-market/market-snapshot?interval=ONE_FOURTH_HOUR&dp=TODAY&showGraph=false&toDate=&fromDate=&_rsc=d60f5"

    def fetch_latest(self):
        import requests
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
            response = requests.get(self.url, headers=headers, timeout=20)
            response.raise_for_status()
            # Try to extract the first table from the HTML
            df = pd.read_html(io.StringIO(response.text))[0]
            logger.info("Successfully fetched latest IEX spot prices using requests.")
            return df
        except Exception as e:
            logger.error(f"Failed to fetch IEX data with requests: {e}")
            return None