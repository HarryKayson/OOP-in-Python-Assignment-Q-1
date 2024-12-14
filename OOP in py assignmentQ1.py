"""
Assignment 1: Design Your Own Class! 🏗️
Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation.
"""
# Base Class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand  # Public attribute
        self.model = model  # Public attribute
        self.__battery_life = battery_life  # Private attribute (encapsulation)

    # Method to display details about the smartphone
    def display_info(self):
        print(f"Smartphone Info:\nBrand: {self.brand}\nModel: {self.model}")
        print(f"Battery Life: {self.__battery_life} hours")

    # Getter method for the private battery_life attribute
    def get_battery_life(self):
        return self.__battery_life

    # Setter method for the private battery_life attribute
    def set_battery_life(self, battery_life):
        if battery_life > 0:
            self.__battery_life = battery_life
        else:
            print("Battery life must be a positive number.")

    # Method for making a call (base class functionality)
    def make_call(self, phone_number):
        print(f"Calling {phone_number}...")

# Derived Class: SmartphoneWithCamera (Inheriting from Smartphone)
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_life, camera_resolution):
        super().__init__(brand, model, battery_life)  # Call the parent class constructor
        self.camera_resolution = camera_resolution  # New attribute for camera resolution

    # Overriding display_info method to include camera resolution
    def display_info(self):
        super().display_info()  # Call the base class display_info method
        print(f"Camera Resolution: {self.camera_resolution} MP")

    # Polymorphism: Method to take a picture
    def take_picture(self):
        print(f"Taking a picture with {self.camera_resolution} MP camera...")

# Creating objects of the classes
smartphone1 = Smartphone("Apple", "iPhone 13", 20)
smartphone_with_camera = SmartphoneWithCamera("Samsung", "Galaxy S21", 22, 108)

# Displaying information about both smartphones
smartphone1.display_info()
print("---")
smartphone_with_camera.display_info()

# Making a call with the base class object
smartphone1.make_call("123-456-7890")

# Taking a picture with the derived class object
smartphone_with_camera.take_picture()

# Accessing and modifying private attribute using getter and setter
print(f"Current battery life of {smartphone1.model}: {smartphone1.get_battery_life()} hours")
smartphone1.set_battery_life(25)  # Modify battery life
print(f"Updated battery life of {smartphone1.model}: {smartphone1.get_battery_life()} hours")

