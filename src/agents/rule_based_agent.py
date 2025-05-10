import logging
from loguru import logger

class RuleBasedAgent:
    def decide_action(self, current_price, forecasted_price, budget):
        if forecasted_price > current_price + 1.0 and budget > 0:
            return {"action": "buy", "quantity": 1}
        elif forecasted_price < current_price - 1.0:
            return {"action": "sell", "quantity": 1}
        else:
            return {"action": "hold"}