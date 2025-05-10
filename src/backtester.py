import pandas as pd

class Backtester:
    def __init__(self, model, agent, executor):
        self.model = model
        self.agent = agent
        self.executor = executor

    def run(self, historical_data):
        results = []
        for _, row in historical_data.iterrows():
            forecast = self.model.predict(row[["hour", "Demand", "Supply"]].to_frame().T)
            decision = self.agent.decide_action(row["Price"], forecast, self.executor.balance)
            old_balance = self.executor.balance
            balance, position = self.executor.execute(decision, row["Price"])
            results.append({
                "timestamp": row["Time"],
                "price": row["Price"],
                "forecast": forecast,
                "action": decision["action"],
                "balance": balance,
                "position": position
            })
        return pd.DataFrame(results)