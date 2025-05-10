from data_fetcher.iex_api import IEXScraper
from models.price_forecaster import PriceForecaster
from agents.rule_based_agent import RuleBasedAgent
from executor.simulated_executor import SimulatedExecutor
from backtester import Backtester
import pandas as pd

def main():
    scraper = IEXScraper()
    df = scraper.fetch_latest()
    if df is None:
        print("Error: Failed to fetch IEX data. No data returned. Please check the data source or your network connection.")
        return
    print("Fetched DataFrame columns:", list(df.columns))
    # Map columns to expected names
    try:
        # Extract the start time from 'Time Block'
        df['Time'] = df['Date'].astype(str) + ' ' + df['Time Block'].str.split(' - ').str[0]
        df['Time'] = pd.to_datetime(df['Time'], format='%d-%m-%Y %H:%M')
        df = df.rename(columns={
            'Purchase Bid (MW)': 'Demand',
            'Sell Bid (MW)': 'Supply',
            'MCP (Rs/MWh) *': 'Price'
        })
        df = df[['Time', 'Demand', 'Supply', 'Price']]
    except Exception as e:
        print(f"Failed to map columns: {e}")
        print(f"Available columns: {list(df.columns)}")
        return

    forecaster = PriceForecaster()
    forecaster.train(df)

    agent = RuleBasedAgent()
    executor = SimulatedExecutor()

    backtester = Backtester(forecaster, agent, executor)
    results = backtester.run(df)
    print(results.head())

    # --- Visualization ---
    import matplotlib.pyplot as plt
    plt.figure(figsize=(14,6))
    plt.plot(results['timestamp'], results['price'], label='Actual Price')
    plt.plot(results['timestamp'], [f[0] for f in results['forecast']], label='Forecasted Price')
    buy_signals = results[results['action'] == 'buy']
    sell_signals = results[results['action'] == 'sell']
    plt.scatter(buy_signals['timestamp'], buy_signals['price'], marker='^', color='g', label='Buy', s=100)
    plt.scatter(sell_signals['timestamp'], sell_signals['price'], marker='v', color='r', label='Sell', s=100)
    plt.legend()
    plt.xlabel('Timestamp')
    plt.ylabel('Price (₹)')
    plt.title('IEX Price, Forecast, and Trading Actions')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()