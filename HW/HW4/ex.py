# Define the Car class (the blueprint for a car)
class Car:
    # The __init__ method is the initializer, called automatically when a new object is created.
    # 'self' refers to the object being created, and 'color' and 'model' are its attributes.
    def __init__(self, color, model):
        self.color = color   # Set the object's color attribute
        self.model = model   # Set the object's model attribute
        self.speed = 0       # The initial speed is set to 0

    # A method to increase the speed by 10 km/h
    def accelerate(self):
        self.speed += 10
        print(f"The current speed of the {self.model} is {self.speed} km/h.")

    # A method to stop the car by setting speed to 0
    def brake(self):
        self.speed = 0
        print(f"The {self.model} has stopped. Current speed is {self.speed} km/h.")

# Create 'objects (instances)' using the Car class
# Create a red Sonata object named my_car
my_car = Car("red", "Sonata")

# Create a blue Avante object named your_car
your_car = Car("blue", "Elantra")

# --- Accessing attributes and calling methods of the objects ---

print(f"My car is a {my_car.color} {my_car.model}.")
print(f"Your car is a {your_car.color} {your_car.model}.")
print("-" * 20)

# Call the accelerate method for the my_car object
my_car.accelerate() # Output: The current speed of the Sonata is 10 km/h.
my_car.accelerate() # Output: The current speed of the Sonata is 20 km/h.

# Call the accelerate method for the your_car object
your_car.accelerate() # Output: The current speed of the Avante is 10 km/h.

print("-" * 20)

# Check the current speed of both my_car and your_car
print(f"Speed of my car ({my_car.model}): {my_car.speed} km/h")
print(f"Speed of your car ({your_car.model}): {your_car.speed} km/h")

print("-" * 20)

# Call the brake method for the my_car object
my_car.brake() # Output: The Sonata has stopped. Current speed is 0 km/h.
