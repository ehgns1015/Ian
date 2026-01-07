


from constants import *

class Validator:
    def validate_white_balls(self, numbers):
        if len(numbers) != WHITE_BALL_COUNT:
            return False
        if len(set(numbers)) != WHITE_BALL_COUNT:
            return False  # Duplicates exist
        for num in numbers:
            if not (WHITE_BALL_MIN <= num <= WHITE_BALL_MAX):
                return False
        return True

    def validate_power_ball(self, number):
        return POWER_BALL_MIN <= number <= POWER_BALL_MAX

    def validate_ticket_count(self, count):
        return count >= 1

    def validate_balance(self, balance, cost):
        return balance >= cost