class SimulatedExecutor:
    def __init__(self, initial_balance=10000):
        self.balance = initial_balance
        self.position = 0

    def execute(self, decision, price):
        if decision["action"] == "buy":
            cost = decision["quantity"] * price
            if self.balance >= cost:
                self.position += decision["quantity"]
                self.balance -= cost
                print(f"Bought {decision['quantity']} units at ₹{price:.2f}")
        elif decision["action"] == "sell":
            if self.position >= decision["quantity"]:
                self.position -= decision["quantity"]
                self.balance += decision["quantity"] * price
                print(f"Sold {decision['quantity']} units at ₹{price:.2f}")
        elif decision["action"] == "hold":
            print("No action taken.")
        return self.balance, self.position