import os
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def solve_non_linear_circuit():
    print("Solving non-linear circuit with a diode")
    input()

def solve_rlc_circuit():
    print("Solving RLC linear circuit")
    input()

def exit_program():
    print("Exiting program")
    exit()

def default():
    print("Invalid option")
    input()
    return

switch_dict = {
    "1": solve_non_linear_circuit,
    "2": solve_rlc_circuit,
    "3": exit_program
}

def switch(option):
    switch_dict.get(option, default)()

while 1:
    print("Welcome to our cool program for solving circuits!")
    print("Please select an option:")
    print("1. Solve a non-linear circuit with a diode")
    print("2. Solve a RLC linear circuit")
    print("3. Exit")

    option = input("Enter your option: ")
    clear_screen()
    switch(option)
    if option != "3":
        clear_screen()
