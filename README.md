Vehicle Class Hierarchy in Python
Overview
This project demonstrates object-oriented programming concepts in Python through a simple class hierarchy modeling different types of vehicles. It features:

Inheritance: A base Vehicle class and specialized Car and Plane subclasses.

Encapsulation: Vehicle details such as make, model, year, and unique IDs.

Polymorphism: Overridden methods like move() to behave differently depending on the vehicle type.

Unique Identifiers: Each vehicle instance gets a unique UUID.

Basic Simulation: Methods to simulate engine start/stop, movement, and vehicle-specific actions like honking for cars or take off/landing for planes.

Classes
1. Vehicle (Base Class)
Attributes: vehicle_id, make, model, year, color, is_moving

Methods:

start_engine()

stop_engine()

move()

stop()

get_info()

2. Car (Inherits Vehicle)
Additional attributes: num_doors, fuel_level

Methods:

honk()

Overridden move() (drives and consumes fuel)

Overridden get_info() (extends base info)

3. Plane (Inherits Vehicle)
Additional attributes: num_engines, altitude

Methods:

take_off()

land()

Overridden move() (flies at altitude)

Overridden get_info() (extends base info)

Usage Example
python
# Create a Car instance
my_car = Car("Toyota", "Camry", 2023, "Blue", 4)
print(my_car.get_info())
print(my_car.start_engine())
print(my_car.move())  # Car-specific move behavior
print(my_car.honk())
print(my_car.stop())
print(my_car.stop_engine())

# Create a Plane instance
my_plane = Plane("Boeing", "747", 2020, "White", 4)
print(my_plane.get_info())
print(my_plane.start_engine())
print(my_plane.take_off())
print(my_plane.move())  # Plane-specific move behavior
print(my_plane.land())
print(my_plane.stop_engine())
Polymorphism
The project showcases polymorphism by creating a list of heterogeneous Vehicle objects (Car and Plane). Calling the same method move() on each object appropriately triggers the subclass-specific implementation.

Requirements
Python 3.x

uuid module (standard Python library)

How to Run
Save the source code to a Python file, e.g., vehicles.py.

Run the file with Python: python vehicles.py.

Observe the printed outputs demonstrating inheritance and polymorphic behavior.

Author
Created by [Your Name or Username]
