import uuid # For generating unique IDs

# Assignment 1: Design Your Own Class (Vehicle) with Inheritance
class Vehicle:
    """
    A base class representing a generic vehicle.
    It includes attributes common to all vehicles and a basic move method.
    """
    def __init__(self, make, model, year, color):
        """
        Constructor to initialize a Vehicle object.
        :param make: The manufacturer of the vehicle.
        :param model: The model name of the vehicle.
        :param year: The manufacturing year of the vehicle.
        :param color: The color of the vehicle.
        """
        self.vehicle_id = str(uuid.uuid4()) # Unique ID for each vehicle
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_moving = False # Initial state

    def start_engine(self):
        """Simulates starting the vehicle's engine."""
        return f"The {self.color} {self.make} {self.model}'s engine is starting."

    def stop_engine(self):
        """Simulates stopping the vehicle's engine."""
        if self.is_moving:
            self.stop() # Ensure vehicle stops before engine stops
        return f"The {self.color} {self.make} {self.model}'s engine is stopping."

    def move(self):
        """
        A generic method for moving. This will be overridden by subclasses
        to demonstrate polymorphism.
        """
        self.is_moving = True
        return f"The {self.make} {self.model} is moving."

    def stop(self):
        """A generic method for stopping."""
        self.is_moving = False
        return f"The {self.make} {self.model} has stopped."

    def get_info(self):
        """Returns a string with basic information about the vehicle."""
        return (f"Vehicle ID: {self.vehicle_id}\n"
                f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Color: {self.color}\n"
                f"Currently moving: {self.is_moving}")

# Derived class: Car (inherits from Vehicle)
class Car(Vehicle):
    """
    Represents a Car, inheriting from Vehicle.
    Adds car-specific attributes like number of doors.
    """
    def __init__(self, make, model, year, color, num_doors):
        """
        Constructor for the Car class.
        Calls the parent Vehicle constructor and adds a new attribute.
        :param num_doors: The number of doors the car has.
        """
        super().__init__(make, model, year, color) # Initialize parent class attributes
        self.num_doors = num_doors
        self.fuel_level = 100 # Car-specific attribute

    def honk(self):
        """Car-specific method: makes a honking sound."""
        return "Beep! Beep!"

    # Activity 2: Polymorphism Challenge! - Overriding move()
    def move(self):
        """
        Overrides the generic move() method to specify car driving behavior.
        🚗
        """
        self.is_moving = True
        self.fuel_level -= 5 # Simulate fuel consumption
        return f"Driving the {self.color} {self.make} {self.model} (Fuel: {self.fuel_level}%). 🚗"

    def get_info(self):
        """
        Overrides the get_info() method to include car-specific details.
        Demonstrates polymorphism by extending the base method.
        """
        base_info = super().get_info()
        return f"{base_info}\nNumber of Doors: {self.num_doors}, Fuel Level: {self.fuel_level}%"

# Derived class: Plane (inherits from Vehicle)
class Plane(Vehicle):
    """
    Represents a Plane, inheriting from Vehicle.
    Adds plane-specific attributes like number of engines.
    """
    def __init__(self, make, model, year, color, num_engines):
        """
        Constructor for the Plane class.
        Calls the parent Vehicle constructor and adds a new attribute.
        :param num_engines: The number of engines the plane has.
        """
        super().__init__(make, model, year, color) # Initialize parent class attributes
        self.num_engines = num_engines
        self.altitude = 0 # Plane-specific attribute

    def take_off(self):
        """Plane-specific method: simulates taking off."""
        if not self.is_moving:
            self.is_moving = True
        self.altitude = 10000 # Set a default cruising altitude
        return f"The {self.make} {self.model} is taking off and ascending to {self.altitude} feet."

    def land(self):
        """Plane-specific method: simulates landing."""
        self.is_moving = False
        self.altitude = 0
        return f"The {self.make} {self.model} is landing."

    # Activity 2: Polymorphism Challenge! - Overriding move()
    def move(self):
        """
        Overrides the generic move() method to specify plane flying behavior.
        ✈️
        """
        self.is_moving = True
        return f"Flying the {self.color} {self.make} {self.model} at {self.altitude} feet. ✈️"

    def get_info(self):
        """
        Overrides the get_info() method to include plane-specific details.
        Demonstrates polymorphism by extending the base method.
        """
        base_info = super().get_info()
        return f"{base_info}\nNumber of Engines: {self.num_engines}, Altitude: {self.altitude} feet"

# --- Demonstration of Class Usage, Inheritance, and Polymorphism ---

print("--- Creating and Interacting with a Car Object ---")
my_car = Car("Toyota", "Camry", 2023, "Blue", 4)
print(my_car.get_info())
print(my_car.start_engine())
print(my_car.move()) # Calls Car's move() method
print(my_car.honk())
print(my_car.get_info())
print(my_car.stop())
print(my_car.stop_engine())
print("\n" + "="*50 + "\n")

print("--- Creating and Interacting with a Plane Object ---")
my_plane = Plane("Boeing", "747", 2020, "White", 4)
print(my_plane.get_info())
print(my_plane.start_engine())
print(my_plane.take_off())
print(my_plane.move()) # Calls Plane's move() method
print(my_plane.get_info())
print(my_plane.land())
print(my_plane.stop_engine())
print("\n" + "="*50 + "\n")

print("--- Polymorphism Challenge: Common Action, Different Behaviors ---")
# Create a list of different vehicle objects
vehicles = [
    Car("Honda", "Civic", 2021, "Red", 4),
    Plane("Airbus", "A380", 2018, "Grey", 4),
    Car("Tesla", "Model 3", 2024, "Black", 4)
]

for vehicle in vehicles:
    print(f"{vehicle.make} {vehicle.model}:")
    print(vehicle.start_engine())
    print(vehicle.move()) # Each object calls its OWN move() method
    if isinstance(vehicle, Car):
        print(vehicle.honk()) # Specific method for Car
    elif isinstance(vehicle, Plane):
        print(vehicle.take_off()) # Specific method for Plane
    print(vehicle.stop())
    print(vehicle.stop_engine())
    print("-" * 20)
