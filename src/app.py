import streamlit as st
import pandas as pd
from data_fetcher.iex_api import IEXScraper
from models.price_forecaster import PriceForecaster
from agents.rule_based_agent import RuleBasedAgent
from executor.simulated_executor import SimulatedExecutor
from backtester import Backtester
import plotly.graph_objects as go

st.set_page_config(layout="wide")

st.title("IEX Market Data Trading Dashboard")

# Example layout
col1, col2 = st.columns([2, 1])
with col1:
    st.header("Main Dashboard")
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

            # Create an interactive Plotly chart
            fig = go.Figure()

            # Add the actual price line
            fig.add_trace(go.Scatter(
                x=results['timestamp'],
                y=results['price'],
                mode='lines',
                name='Actual Price',
                line=dict(color='blue')
            ))

            # Add the forecasted price line
            fig.add_trace(go.Scatter(
                x=results['timestamp'],
                y=[f[0] for f in results['forecast']],
                mode='lines',
                name='Forecasted Price',
                line=dict(color='orange', dash='dash')
            ))

            # Add buy signals as scatter points
            buy_signals = results[results['action'] == 'buy']
            fig.add_trace(go.Scatter(
                x=buy_signals['timestamp'],
                y=buy_signals['price'],
                mode='markers',
                name='Buy',
                marker=dict(color='green', symbol='triangle-up', size=10)
            ))

            # Add sell signals as scatter points
            sell_signals = results[results['action'] == 'sell']
            fig.add_trace(go.Scatter(
                x=sell_signals['timestamp'],
                y=sell_signals['price'],
                mode='markers',
                name='Sell',
                marker=dict(color='red', symbol='triangle-down', size=10)
            ))

            # Update layout for better visualization
            fig.update_layout(
                title="IEX Price, Forecast, and Trading Actions",
                xaxis_title="Timestamp",
                yaxis_title="Price (₹)",
                legend_title="Legend",
                template="plotly_white",
                xaxis=dict(showgrid=True),
                yaxis=dict(showgrid=True)
            )

            # Render the Plotly chart in Streamlit
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Failed to fetch data from IEX.")

with col2:
    st.header("Sidebar")
    st.write("Additional Controls")

st.info("Click the button above to fetch the latest IEX market data and run your trading model.")
