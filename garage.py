import os
import platform
import json
from enum import Enum


class Actions(Enum):
    EXIT = 1
    ADD = 2
    DELETE = 3
    DISPLAY = 4
    FIND = 5

cars = []
File_Name = "cars.txt"
next_car_id = 0 

def menu():
    for act in Actions: 
        print(f"{act.value} - {act.name}" )
    while True:
            user_select = int(input("What would you like to do? "))
            return user_select
        
def clear_terminal():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def add_car():
    global next_car_id
    car_brand = input("Car brand: ")
    car_color = input("Car color: ")
    car_model = int(input("Car model: "))
    cars.append({"id": next_car_id, "brand": car_brand, "color": car_color, "model": car_model})
    next_car_id += 1
    save_cars_to_files()

def print_cars():
    if not cars:
        print("No cars available.")
    else:
        for car in cars:
            print(f"Brand: {car['brand']}, Model: {car['model']}, Color: {car['color']}.")

def delete_car():
    car_found = False
    car_brand = input("Car brand: ")
    car_color = input("Car color: ")
    car_model = int(input("Car model: "))
    for car in cars:
        if car["brand"] == car_brand and car["color"] == car_color and car["model"] == car_model:
            cars.remove(car)
            car_found = True
            break

    if not car_found:
        print("This car does not exist...")
    
    save_cars_to_files()

def find_car():
    car_found = False
    car_brand = input("Car brand: ")
    car_color = input("Car color: ")
    car_model = int(input("Car model: "))
    for car in cars:
        if car["brand"] == car_brand and car["color"] == car_color and car["model"] == car_model:
            print(car)
            car_found = True
            break
    if not car_found:
        print("This car does not exist...")

def save_cars_to_files():
    try:
        with open(File_Name, 'w') as file:
            json.dump(cars, file)
    except Exception as e:
        print(f"Error saving cars to file: {e}")

def load_cars_from_file():
    global cars, next_car_id
    try:
        with open(File_Name, 'r') as file:
            cars = json.load(file)
        if cars:
            next_car_id = max(car['id'] for car in cars) + 1  # Set next ID to be max ID + 1
    except FileNotFoundError:
        print(f"The file {File_Name} was not found. Starting with an empty car list.")
    except json.JSONDecodeError:
        print(f"The file {File_Name} is not a valid JSON. Starting with an empty car list.")
    except Exception as e:
        print(f"An error occurred while loading the file: {e}. Starting with an empty car list.")

if __name__ == "__main__":
    load_cars_from_file()

    while True:
        user_select = menu()
        clear_terminal()
        if user_select == (Actions.EXIT).value:
            exit()
        elif user_select == (Actions.ADD).value:
            add_car()
        elif user_select == (Actions.DISPLAY).value:
            print_cars()
        elif user_select == (Actions.DELETE).value:
            delete_car()
        elif user_select == (Actions.FIND).value:
            find_car()
        else:
            print("Please select an option from the menu.")


