

import random
from constants import *
from lottery_ticket import LotteryTicket
from validator import Validator


class LotteryMachine:
    def __init__(self):
        self.winning_ticket = None
        self.validator = Validator()

    def generate_random_ticket(self):
        whites = random.sample(range(WHITE_BALL_MIN, WHITE_BALL_MAX + 1), WHITE_BALL_COUNT)
        pb = random.randint(POWER_BALL_MIN, POWER_BALL_MAX)
        return LotteryTicket(whites, pb)

    def create_manual_ticket(self, white_balls, power_ball):
        # This assumes the numbers were already checked by the validator in main.py
        return LotteryTicket(white_balls, power_ball)

    def draw_winning_numbers(self):
        self.winning_ticket = self.generate_random_ticket()

    def get_winning_ticket(self):
        return self.winning_ticket

    def check_ticket(self, ticket):
        user_whites = set(ticket.get_white_balls())
        win_whites = set(self.winning_ticket.get_white_balls())

        matches = len(user_whites & win_whites)
        pb_match = ticket.get_power_ball() == self.winning_ticket.get_power_ball()

        return {
            "white_matches": matches,
            "power_match": pb_match,
            "is_jackpot": (matches == WHITE_BALL_COUNT and pb_match)
        }