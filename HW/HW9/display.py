class Display:
    def show_welcome(self):
        print("=" * 40)
        print("      WELCOME TO LOTTERY SIMULATOR")
        print("=" * 40)

    def show_ticket(self, ticket, number=None):
        prefix = f"{number}. " if number else "Generated: "
        print(f"  {prefix}{ticket}")

    def show_all_tickets(self, tickets):
        print("\n" + "=" * 40)
        print("           YOUR TICKETS")
        print("=" * 40)
        for i, t in enumerate(tickets, 1):
            self.show_ticket(t, i)

    def show_winning_numbers(self, ticket):
        print("\n" + "=" * 40)
        print("     DRAWING WINNING NUMBERS...")
        print("=" * 40)
        print(f"  Winning Numbers: {ticket}")

    def show_result(self, ticket_num, result):
        pb_text = "YES" if result["power_match"] else "NO"
        print(f"  Ticket {ticket_num}: {result['white_matches']} white balls | Power Ball: {pb_text}")

    def show_summary(self, count, spent, remaining):
        print("\n" + "=" * 40)
        print("             SUMMARY")
        print("=" * 40)
        print(f"  Tickets purchased: {count}")
        print(f"  Money spent: ${spent}")
        print(f"  Remaining balance: ${remaining:.2f}")

    def show_error(self, message):
        print(f"  ERROR: {message}")