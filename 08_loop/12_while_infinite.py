"""
While Loop - Infinite Loops and Control

Infinite loops run until explicitly broken using:
- break statement
- return statement (in functions)
- System interrupt

Common pattern: while True with break conditions

Source: 02_while_loops.docx - Infinite Loops and Loop Control
"""

# Basic infinite loop pattern (demonstration only)
print("=== INFINITE LOOP PATTERN ===\n")
print("Infinite loop with break condition:\n")

count = 0
while True:
    print(f"Iteration {count}")
    count += 1
    if count >= 5:
        break

print("Loop exited")

# Menu system pattern
print("\n=== MENU SYSTEM PATTERN ===\n")

# Simulated menu choices
choices = ['1', '2', '3', '4']
choice_index = 0

while True:
    print("\n--- Menu ---")
    print("1. Option One")
    print("2. Option Two")
    print("3. Option Three")
    print("4. Exit")

    # Simulate user choice
    choice = choices[choice_index]
    print(f"Choice: {choice}")

    if choice == '1':
        print("You selected Option One")
    elif choice == '2':
        print("You selected Option Two")
    elif choice == '3':
        print("You selected Option Three")
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice")

    choice_index += 1

# Server simulation
print("\n=== SERVER LOOP SIMULATION ===\n")

requests = ['GET', 'POST', 'GET', 'DELETE', 'SHUTDOWN']
request_index = 0

print("Server starting...")
while True:
    # Simulate receiving request
    if request_index >= len(requests):
        break

    request = requests[request_index]
    print(f"Received: {request}")

    if request == 'SHUTDOWN':
        print("Shutdown signal received")
        break

    # Process request
    print(f"Processing {request} request...")
    request_index += 1

print("Server stopped")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Retry until success
print("=== RETRY MECHANISM ===")
attempt = 0
max_attempts = 5
success = False

while True:
    attempt += 1
    print(f"Attempt {attempt}")

    # Simulate success on 3rd attempt
    if attempt == 3:
        success = True
        print("Success!")
        break

    if attempt >= max_attempts:
        print("Maximum attempts reached")
        break

# Example 2: Process until flag set
print("\n=== PROCESS UNTIL FLAG ===")
processing = True
items_processed = 0

while processing:
    items_processed += 1
    print(f"Processing item {items_processed}")

    # Simulate completion condition
    if items_processed >= 5:
        processing = False
        print("All items processed")

# Example 3: Game loop
print("\n=== GAME LOOP ===")
game_running = True
round_number = 0

while game_running:
    round_number += 1
    print(f"\nRound {round_number}")

    # Simulate game rounds
    if round_number >= 3:
        print("Game Over!")
        game_running = False

# Example 4: Multiple break conditions
print("\n=== MULTIPLE BREAK CONDITIONS ===")
temperature = 20
pressure = 50
iteration = 0

while True:
    iteration += 1
    temperature += 5
    pressure += 10

    print(f"Iteration {iteration}: Temp={temperature}, Pressure={pressure}")

    if temperature > 100:
        print("Temperature critical!")
        break

    if pressure > 150:
        print("Pressure critical!")
        break

    if iteration >= 10:
        print("Maximum iterations reached")
        break

# Example 5: Continue with infinite loop
print("\n=== CONTINUE IN INFINITE LOOP ===")
counter = 0

while True:
    counter += 1

    # Skip multiples of 3
    if counter % 3 == 0:
        if counter >= 15:
            break
        continue

    print(counter, end=" ")

print()

# Example 6: Nested infinite loops
print("\n=== NESTED INFINITE LOOPS ===")
outer_count = 0

while True:
    outer_count += 1
    inner_count = 0

    while True:
        inner_count += 1
        print(f"Outer: {outer_count}, Inner: {inner_count}")

        if inner_count >= 2:
            break

    if outer_count >= 2:
        break

# Example 7: While True with complex condition
print("\n=== COMPLEX EXIT CONDITION ===")
score = 0
lives = 3
max_score = 50

while True:
    score += 10

    # Simulate losing a life
    if score >= 20 and lives > 1:
        lives -= 1
        print(f"Lost a life! Score={score}, Lives={lives}")
    else:
        print(f"Score={score}, Lives={lives}")

    # Check win/loss conditions
    if score >= max_score:
        print("You win!")
        break

    if lives <= 0:
        print("Game over!")
        break

# Example 8: Event loop simulation
print("\n=== EVENT LOOP ===")
events = ['click', 'hover', 'click', 'keypress', 'quit']
event_index = 0

print("Event loop starting...")
while True:
    if event_index >= len(events):
        break

    event = events[event_index]
    print(f"Event: {event}")

    if event == 'quit':
        print("Quit event received")
        break

    # Handle event
    print(f"Handling {event}...")
    event_index += 1

# Example 9: Producer-consumer pattern
print("\n=== PRODUCER-CONSUMER ===")
queue = []
items_to_produce = 5
items_produced = 0

while True:
    # Produce
    if items_produced < items_to_produce:
        queue.append(f"item_{items_produced}")
        items_produced += 1
        print(f"Produced item {items_produced}")

    # Consume
    if queue:
        item = queue.pop(0)
        print(f"Consumed {item}")

    # Exit condition
    if items_produced >= items_to_produce and len(queue) == 0:
        print("All items produced and consumed")
        break

# Example 10: Timeout pattern
print("\n=== TIMEOUT PATTERN ===")
max_time = 10
elapsed_time = 0
task_complete = False

while True:
    elapsed_time += 1
    print(f"Time: {elapsed_time}s")

    # Simulate task completion
    if elapsed_time == 5:
        task_complete = True
        print("Task completed!")
        break

    # Timeout check
    if elapsed_time >= max_time:
        print("Timeout!")
        break

# Important note
print("\n=== IMPORTANT NOTE ===")
print("In real applications, be careful with infinite loops!")
print("Always ensure there's a way to exit (break condition).")
print("In interactive programs, consider using try-except for KeyboardInterrupt.")
print("\nExample pattern:")
print("try:")
print("    while True:")
print("        # your code")
print("        pass")
print("except KeyboardInterrupt:")
print("    print('\\nExiting...')")
