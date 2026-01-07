from constants import TICKET_PRICE
from validator import Validator
from lottery_machine import LotteryMachine
from player import Player
from display import Display


def get_manual_numbers(validator, display):
    while True:
        try:
            raw_whites = input("  Enter 5 white balls (1-69) separated by spaces: ")
            whites = [int(n) for n in raw_whites.split()]
            if not validator.validate_white_balls(whites):
                display.show_error("Invalid white balls. Ensure they are 1-69 and unique.")
                continue

            pb = int(input("  Enter power ball (1-26): "))
            if not validator.validate_power_ball(pb):
                display.show_error("Invalid Power Ball.")
                continue

            return whites, pb
        except ValueError:
            display.show_error("Please enter numbers only.")


def main():
    display = Display()
    machine = LotteryMachine()
    validator = Validator()

    display.show_welcome()

    try:
        start_bal = float(input("Enter starting balance: $"))
        player = Player(start_bal)
    except ValueError:
        return

    try:
        count = int(input("How many tickets would you like to buy? "))
        if not validator.validate_balance(player.get_balance(), count * TICKET_PRICE):
            display.show_error("Not enough money!")
            return
    except ValueError:
        return

    for i in range(count):
        print(f"\n--- Ticket {i + 1} ---")
        choice = input("  Manual (M) or Random (R)? ").upper()

        if choice == 'M':
            whites, pb = get_manual_numbers(validator, display)
            from lottery_ticket import LotteryTicket
            ticket = LotteryTicket(whites, pb)
        else:
            ticket = machine.generate_random_ticket()

        player.buy_ticket(ticket)
        display.show_ticket(ticket)

    display.show_all_tickets(player.get_tickets())
    machine.draw_winning_numbers()
    display.show_winning_numbers(machine.get_winning_ticket())

    print("\n" + "=" * 40 + "\n            RESULTS\n" + "=" * 40)
    any_jackpot = False
    for i, ticket in enumerate(player.get_tickets(), 1):
        res = machine.check_ticket(ticket)
        display.show_result(i, res)
        if res["is_jackpot"]: any_jackpot = True

    if any_jackpot:
        print("\nJACKPOT! You are a winner!")
    else:
        print("\nNo jackpot winner this time.")

    display.show_summary(len(player.get_tickets()), len(player.get_tickets()) * TICKET_PRICE, player.get_balance())


if __name__ == "__main__":
    main()
