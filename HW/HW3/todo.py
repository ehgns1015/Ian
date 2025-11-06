# ===== TO-DO LIST =====
# 1. Add Task
# 2. View Tasks
# 3. Remove Task
# 4. Exit
# Select an option: 1
# Enter the task to add: Finish homework
# Task 'Finish homework' added.

#===== TO-DO LIST =====
#1. Add Task
#2. View Tasks
#3. Remove Task
#4. Exit
#Select an option: 1
#Enter the task to add: Walk the dog
#Task 'Walk the dog' added.

#===== TO-DO LIST =====
#1. Add Task
#2. View Tasks
#3. Remove Task
#4. Exit
#Select an option: 2

#--- Your Tasks ---
#1. Finish homework
#2. Walk the dog

#===== TO-DO LIST =====
#1. Add Task
#2. View Tasks
#3. Remove Task
#4. Exit
#Select an option: 3
#--- Your Tasks ---
#1. Finish homework
#2. Walk the dog
#Enter the task number to remove: 2
#Task 'Walk the dog' removed.

#===== TO-DO LIST =====
#1. Add Task
#2. View Tasks
#3. Remove Task
#4. Exit
#Select an option: 1
#Enter the task to add: Buy groceries
#Task 'Buy groceries' added.

#===== TO-DO LIST =====
#1. Add Task
#2. View Tasks
#3. Remove Task
#4. Exit
#Select an option: 2

#--- Your Tasks ---
#1. Finish homework
#2. Buy groceries

#===== TO-DO LIST =====
#1. Add Task
#2. View Tasks
#3. Remove Task
#4. Exit
#Select an option: 5
#Invalid option. Please try again.

#===== TO-DO LIST =====
#1. Add Task
#2. View Tasks
#3. Remove Task
#4. Exit
#Select an option: 4
#Exiting application.

# 1. Define a function to display the main menu.
#    - Function name: display_menu
#    - Purpose: To print the menu options (1: Add, 2: View, 3: Remove, 4: Exit) to the console.
#    - This function doesn't need to take any parameters.
def display_menu():
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


# 2. Define a function to add a new task.
#    - Function name: add_task
#    - Parameter(s): It needs to take the 'tasks' list as an argument.
#    - Implementation:
#      a. Prompt the user to enter a new task using input().
#      b. Use the .append() method to add the new task (a string) to the 'tasks' list.
#      c. Print a confirmation message.
def add_task(tasks, new_task):
    print("enter the task to add")
    tasks.append(new_task)
    print(f"Task '{new_task}' added.")
# 3. Define a function to view all tasks.
#    - Function name: view_tasks
#    - Parameter(s): It needs to take the 'tasks' list as an argument.
#    - Implementation:
#      a. Use an 'if-else' statement to check if the 'tasks' list is empty.
#         - Hint: An easy way to check if a list is empty is 'if not tasks:'.
#      b. If the list is empty, print a message saying there are no tasks.
#      c. If the list is not empty, use a 'for' loop to iterate through the tasks.
#         - Hint: Use the enumerate() function to get both the index and the task.
#         - Remember that users see a 1-based list, so print the index plus 1.
def view_tasks(tasks):
    if not tasks:
        print("There are no tasks.")
    else:
        print("Your tasks:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")



# 4. Define a function to remove a task.
#    - Function name: remove_task
#    - Parameter(s): It needs to take the 'tasks' list as an argument.
#    - Implementation:
#      a. First, call the view_tasks() function to show the user the numbered list.
#      b. Prompt the user to enter the number of the task to remove.
#      c. Use a try-except block to handle potential errors (e.g., if the user enters text or a number that doesn't exist).
#         - Inside the 'try' block, convert the user's input to an integer.
#         - Subtract 1 from the user's input to get the correct zero-based index for the list.
#         - Use the .pop() method with this index to remove the task.
#         - Print a confirmation message.
#      d. Inside the 'except' block, handle ValueError and IndexError. Print an appropriate error message for each case.
def remove_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return  # Exit early if there are no tasks

    try:
        task_num = int(input("Enter the number of the task to remove: "))
        task_index = task_num - 1  # Convert to 0-based index
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task}' has been removed.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except IndexError:
        print("Invalid task number. Please choose a number from the list.")
