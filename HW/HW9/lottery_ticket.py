class LotteryTicket:
    def __init__(self, white_balls, power_ball):
        self.white_balls = sorted(white_balls)
        self.power_ball = power_ball

    def __str__(self):
        # Format: 05-12-23-45-67 | PB: 14
        whites = "-".join([f"{num:02d}" for num in self.white_balls])
        return f"{whites} | PB: {self.power_ball:02d}"

    def get_white_balls(self):
        return self.white_balls

    def get_power_ball(self):
        return self.power_ball