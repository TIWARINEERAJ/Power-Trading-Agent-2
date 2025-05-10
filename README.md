
⚡ Power Trading Agent for IEX (India)
A full-stack, agentic AI platform for automated trading, forecasting, and analytics on the Indian Energy Exchange (IEX). This project features real-time data scraping, price forecasting, rule-based trading, and a beautiful Streamlit dashboard for visualization and control.

🚀 Features
Live IEX Market Data Scraping (Selenium, pandas)
Spot Price Forecasting (Random Forest, scikit-learn)
Rule-Based Trading Agent (customizable logic)
Backtesting Engine (simulate trades, balance, and position)
Interactive Streamlit Dashboard
Rich Visualizations (matplotlib)
Modular, Extensible Codebase
Ready for Cloud Deployment (Streamlit Cloud)
📊 Demo
Add a screenshot or GIF here after your first deployment!

🏗️ Project Structure
CopyInsert
├── src/
│   ├── app.py                # Streamlit frontend
│   ├── main.py               # CLI entry point
│   ├── data_fetcher/
│   │   └── iex_api.py        # Selenium-based IEX scraper
│   ├── models/
│   │   └── price_forecaster.py
│   ├── agents/
│   │   └── rule_based_agent.py
│   ├── executor/
│   │   └── simulated_executor.py
│   ├── backtester.py         # Backtesting logic
│   └── ...
├── requirements.txt
├── Dockerfile (optional)
├── README.md
└── ...
⚙️ Setup & Installation
Clone the repository:
sh
CopyInsert
git clone https://github.com/TIWARINEERAJ/power-trading-agent.git
cd power-trading-agent
Install dependencies:
sh
CopyInsert
pip install -r requirements.txt
(Optional) Install ChromeDriver:
Make sure ChromeDriver is installed and in your PATH for Selenium scraping.
Or use webdriver-manager for automatic driver management.
🖥️ Local Usage
Run the CLI version:
sh
CopyInsert
python src/main.py
Run the Streamlit Dashboard:
sh
CopyInsert
streamlit run src/app.py
☁️ Deploy on Streamlit Community Cloud
Push your code to GitHub (see instructions above).
Go to Streamlit Cloud
Connect your repo and set the entry point to src/app.py.
Click Deploy!
🧠 How It Works
Data Fetching: Uses Selenium to scrape the latest market snapshot from IEX India, handling dynamic JavaScript content.
Data Processing: Cleans and transforms the table for model input.
Forecasting: Trains a Random Forest model on demand, supply, and time features.
Trading Agent: Makes buy/sell/hold decisions using customizable rule-based logic.
Backtesting: Simulates trades, tracks balance and position, and outputs results.
Visualization: Streamlit UI displays tables, charts, and trading actions interactively.
📱 Features Roadmap
[x] Real-time scraping and visualization
[x] Backtesting and performance metrics
[x] Interactive dashboard
[ ] User authentication and personalized order history
[ ] Price charts with longer historical data
[ ] Market analysis tools (volume indicators, price trends)
[ ] Mobile-responsive design improvements
[ ] Order cancellation functionality
[ ] Email notifications for completed trades
🛠️ Customization
Trading Logic: Edit src/agents/rule_based_agent.py to modify your trading rules.
Model: Swap out the Random Forest for any scikit-learn compatible regressor in src/models/price_forecaster.py.
Scraper: Update selectors or URLs in src/data_fetcher/iex_api.py if the IEX site changes.
🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

📄 License
This project is licensed under the MIT License.

🙋‍♂️ Support & Contact
For questions, suggestions, or support, open an issue or contact @TIWARINEERAJ.

🌱 Acknowledgements
IEX India
Streamlit
scikit-learn
Selenium
pandas
matplotlib