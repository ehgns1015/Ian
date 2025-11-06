# Define the Fighter class (the blueprint for a fighter)
class Fighter:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    # Method to attack an opponent
    def attack(self, other_fighter):
        other_fighter.health -= self.attack_power
        print(f"{self.name} attacks {other_fighter.name}!")
        print(f"  -> {other_fighter.name}'s remaining health: {other_fighter.health}")

    # Method to check if the fighter is alive
    def is_alive(self):
        return self.health > 0

# --- Create Fighter objects ---
# fighter1: high attack power, low health
fighter1 = Fighter("Warrior A", 100, 15)
# fighter2: low attack power, high health
fighter2 = Fighter("Mage B", 120, 10)

print(f"{fighter1.name} (Health: {fighter1.health}, Attack Power: {fighter1.attack_power}) vs. {fighter2.name} (Health: {fighter2.health}, Attack Power: {fighter2.attack_power})\n")

# --- Battle Simulation ---
turn = 0
while fighter1.is_alive() and fighter2.is_alive():
    turn += 1
    print(f"--- Turn {turn} ---")

    # fighter1 attacks
    fighter1.attack(fighter2)
    if not fighter2.is_alive():
        break

    # fighter2 attacks
    fighter2.attack(fighter1)
    if not fighter1.is_alive():
        break

# --- Battle Over ---
print("\n--- Battle Over ---")
if fighter1.is_alive():
    print(f"{fighter1.name} wins! They have {fighter1.health} health left")
else:
    print(f"{fighter2.name} wins! They have {fighter2.health} health left")
