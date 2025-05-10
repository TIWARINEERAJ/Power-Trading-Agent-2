import streamlit as st
import pandas as pd
from data_fetcher.iex_api import IEXScraper
from models.price_forecaster import PriceForecaster
from agents.rule_based_agent import RuleBasedAgent
from executor.simulated_executor import SimulatedExecutor
from backtester import Backtester

st.title("IEX Market Data Trading Dashboard")

if st.button("Fetch Latest Data and Run Model"):
    scraper = IEXScraper()
    df = scraper.fetch_latest()
    if df is not None:
        st.write("Fetched DataFrame columns:", list(df.columns))
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
            st.error(f"Failed to map columns: {e}")
            st.write(f"Available columns: {list(df.columns)}")
            st.stop()
        forecaster = PriceForecaster()
        forecaster.train(df)
        agent = RuleBasedAgent()
        executor = SimulatedExecutor()
        backtester = Backtester(forecaster, agent, executor)
        results = backtester.run(df)
        st.subheader("Results Table")
        st.dataframe(results)
        st.subheader("Price, Forecast, and Trading Actions")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(14,6))
        ax.plot(results['timestamp'], results['price'], label='Actual Price')
        ax.plot(results['timestamp'], [f[0] for f in results['forecast']], label='Forecasted Price')
        buy_signals = results[results['action'] == 'buy']
        sell_signals = results[results['action'] == 'sell']
        ax.scatter(buy_signals['timestamp'], buy_signals['price'], marker='^', color='g', label='Buy', s=100)
        ax.scatter(sell_signals['timestamp'], sell_signals['price'], marker='v', color='r', label='Sell', s=100)
        ax.legend()
        ax.set_xlabel('Timestamp')
        ax.set_ylabel('Price (₹)')
        ax.set_title('IEX Price, Forecast, and Trading Actions')
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)
    else:
        st.error("Failed to fetch data from IEX.")

st.info("Click the button above to fetch the latest IEX market data and run your trading model.")
