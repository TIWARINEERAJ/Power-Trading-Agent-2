import requests
import pandas as pd
import io
from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class IEXScraper:
    def __init__(self):
        self.url = "https://www.iexindia.com/market-data/day-ahead-market/market-snapshot?interval=ONE_FOURTH_HOUR&dp=TODAY&showGraph=false&toDate=&fromDate=&_rsc=d60f5"

    def fetch_latest(self):
        try:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--window-size=1920,1080')

            # If chromedriver is not in PATH, specify the executable_path argument
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(self.url)

            # Wait for the table to load (update the selector as needed)
            try:
                table = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.TAG_NAME, "table"))
                )
            except Exception as e:
                logger.error(f"Table not found on the page: {e}")
                driver.quit()
                return None

            html = table.get_attribute('outerHTML')
            df = pd.read_html(io.StringIO(html))[0]
            logger.info("Successfully fetched latest IEX spot prices using Selenium.")
            driver.quit()
            return df
        except Exception as e:
            logger.error(f"Failed to fetch IEX data with Selenium: {e}")
            return None