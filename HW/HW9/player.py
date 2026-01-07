


from constants import TICKET_PRICE

class Player:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.tickets = []

    def get_balance(self):
        return self.balance

    def get_tickets(self):
        return self.tickets

    def get_ticket_count(self):
        """Return the number of tickets currently owned by the player"""
        return len(self.tickets)

    def can_afford(self, amount):
        return self.balance >= amount

    def deduct_balance(self, amount):
        """Subtracts the cost from the player's wallet"""
        self.balance -= amount

    def add_ticket(self, ticket):
        """Adds a ticket object to the player's collection"""
        self.tickets.append(ticket)

    def buy_ticket(self, ticket):
        if self.can_afford(TICKET_PRICE):
            self.balance -= TICKET_PRICE
            self.tickets.append(ticket)
            return True
        return False