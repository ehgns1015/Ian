"""
While Loop with Conditions

While loops can use complex conditions including:
- Boolean variables
- Comparison operators
- Logical operators (and, or, not)
- Multiple conditions

Source: 02_while_loops.docx - Conditional While Loops
"""

# While with boolean variable
print("=== BOOLEAN CONDITION ===\n")

is_running = True
count = 0

while is_running:
    print(f"Count: {count}")
    count += 1
    if count >= 5:
        is_running = False

# While with comparison
print("\n=== COMPARISON CONDITION ===\n")

temperature = 100

while temperature > 0:
    print(f"Temperature: {temperature}°C")
    temperature -= 10

# While with logical AND
print("\n=== AND CONDITION ===\n")

x = 0
y = 5

while x < 5 and y > 0:
    print(f"x={x}, y={y}")
    x += 1
    y -= 1

# While with logical OR
print("\n=== OR CONDITION ===\n")

balance = 50
debt = 100

print(f"Starting: Balance=${balance}, Debt=${debt}")
while balance < 100 or debt > 0:
    balance += 10
    debt -= 10
    print(f"Balance=${balance}, Debt=${debt}")

# While with NOT
print("\n=== NOT CONDITION ===\n")

found = False
attempts = 0

while not found:
    attempts += 1
    print(f"Attempt {attempts}")
    if attempts >= 3:
        found = True

print("Found!")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Input validation (simulated)
print("=== INPUT VALIDATION ===")
valid_input = False
attempt = 0
inputs = ["abc", "-5", "10"]  # Simulated inputs

while not valid_input and attempt < len(inputs):
    user_input = inputs[attempt]
    print(f"Input: {user_input}")

    if user_input.isdigit() and int(user_input) > 0:
        value = int(user_input)
        print(f"Valid input: {value}")
        valid_input = True
    else:
        print("Invalid input. Please enter a positive number.")

    attempt += 1

# Example 2: Game loop simulation
print("\n=== GAME LOOP ===")
player_health = 100
enemy_health = 100

round_num = 0
while player_health > 0 and enemy_health > 0:
    round_num += 1
    damage = 20

    # Player attacks
    enemy_health -= damage
    print(f"Round {round_num}: Player attacks! Enemy health: {enemy_health}")

    if enemy_health <= 0:
        break

    # Enemy attacks
    player_health -= damage
    print(f"Round {round_num}: Enemy attacks! Player health: {player_health}")

if player_health > 0:
    print("Player wins!")
else:
    print("Enemy wins!")

# Example 3: Resource management
print("\n=== RESOURCE MANAGEMENT ===")
cpu_usage = 90
memory_usage = 80
max_cpu = 95
max_memory = 85

print(f"Initial: CPU={cpu_usage}%, Memory={memory_usage}%")
iteration = 0

while cpu_usage < max_cpu or memory_usage < max_memory:
    iteration += 1
    cpu_usage += 1
    memory_usage += 1
    print(f"Iteration {iteration}: CPU={cpu_usage}%, Memory={memory_usage}%")

    if iteration >= 10:
        break

print("Resource limit approached")

# Example 4: Multiple exit conditions
print("\n=== MULTIPLE EXIT CONDITIONS ===")
score = 0
lives = 3
max_score = 50

print(f"Starting: Score={score}, Lives={lives}")
turn = 0

while score < max_score and lives > 0:
    turn += 1
    score += 10

    # Simulate losing a life occasionally
    if turn % 3 == 0:
        lives -= 1
        print(f"Turn {turn}: Lost a life! Score={score}, Lives={lives}")
    else:
        print(f"Turn {turn}: Score={score}, Lives={lives}")

if score >= max_score:
    print("Victory! Maximum score reached!")
else:
    print("Game over! No lives remaining.")

# Example 5: Timeout with condition
print("\n=== TIMEOUT CONDITION ===")
connected = False
attempts = 0
max_attempts = 5

while not connected and attempts < max_attempts:
    attempts += 1
    print(f"Connection attempt {attempts}...")

    # Simulate successful connection on 3rd attempt
    if attempts == 3:
        connected = True
        print("Connected!")
    else:
        print("Failed. Retrying...")

if not connected:
    print("Connection timeout")

# Example 6: Threshold monitoring
print("\n=== THRESHOLD MONITORING ===")
pressure = 0
temperature = 0
max_pressure = 100
max_temperature = 150

while pressure < max_pressure and temperature < max_temperature:
    pressure += 15
    temperature += 20
    print(f"Pressure={pressure}, Temperature={temperature}")

    if pressure >= max_pressure:
        print("Pressure threshold reached!")
    if temperature >= max_temperature:
        print("Temperature threshold reached!")

# Example 7: While with complex boolean logic
print("\n=== COMPLEX CONDITION ===")
level = 1
experience = 0
max_level = 5
experience_threshold = 100

while level < max_level and (experience < experience_threshold or level == 1):
    experience += 30

    if experience >= experience_threshold:
        level += 1
        experience = 0
        print(f"Level up! Now level {level}")
    else:
        print(f"Level {level}, Experience: {experience}")

# Example 8: Nested condition checks
print("\n=== NESTED CONDITIONS ===")
authenticated = False
session_active = False
retry_count = 0
max_retries = 3

# Simulated auth attempts
auth_attempts = [False, False, True]

while retry_count < max_retries and not authenticated:
    authenticated = auth_attempts[retry_count]
    retry_count += 1

    if authenticated:
        session_active = True
        print(f"Login successful after {retry_count} attempt(s)")
    else:
        print(f"Login failed. Attempt {retry_count}/{max_retries}")

if authenticated and session_active:
    print("User session is active")
else:
    print("Login failed")

# Example 9: Rate limiting
print("\n=== RATE LIMITING ===")
requests_made = 0
max_requests = 10
errors = 0
max_errors = 3

while requests_made < max_requests and errors < max_errors:
    requests_made += 1

    # Simulate occasional errors
    if requests_made % 4 == 0:
        errors += 1
        print(f"Request {requests_made}: Error! (Total errors: {errors})")
    else:
        print(f"Request {requests_made}: Success")

if errors >= max_errors:
    print("Too many errors, stopping requests")
else:
    print("All requests completed")

# Example 10: While until stable
print("\n=== WAIT FOR STABILITY ===")
current_value = 100
target = 50
tolerance = 5
stable_count = 0
required_stable = 3

while abs(current_value - target) > tolerance or stable_count < required_stable:
    # Move toward target
    if current_value > target:
        current_value -= 8
    elif current_value < target:
        current_value += 8

    print(f"Current: {current_value}, Target: {target}")

    # Check stability
    if abs(current_value - target) <= tolerance:
        stable_count += 1
        print(f"  Stable reading {stable_count}/{required_stable}")
    else:
        stable_count = 0

print("System stabilized")
