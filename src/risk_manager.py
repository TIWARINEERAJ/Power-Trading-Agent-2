class RiskManager:
    def __init__(self, max_position=10, max_daily_loss=500):
        self.max_position = max_position
        self.max_daily_loss = max_daily_loss
        self.daily_pnl = 0

    def check_position(self, new_position, current_position):
        return current_position + new_position <= self.max_position

    def check_loss(self, pnl):
        self.daily_pnl += pnl
        return abs(self.daily_pnl) < self.max_daily_loss