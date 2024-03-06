from colorist import red, green, blue, yellow, magenta, cyan, white
import time
import random
import os
from simple_term_menu import TerminalMenu

def launch():
    os.system("clear")
    green("W")
    time.sleep(0.1)
    os.system("clear")
    green("We")
    time.sleep(0.1)
    os.system("clear")
    green("Wel")
    time.sleep(0.1)
    os.system("clear")
    green("Welc")
    time.sleep(0.1)
    os.system("clear")
    green("Welco")
    time.sleep(0.1)
    os.system("clear")
    green("Welcom")
    time.sleep(0.1)
    os.system("clear")
    green("Welcome")
    time.sleep(0.1)
    os.system("clear")
    green("Welcome ")
    time.sleep(0.1)
    os.system("clear")
    green("Welcome t")
    time.sleep(0.1)
    os.system("clear")
    green("Welcome to")
    time.sleep(0.1)
    os.system("clear")
    green("Welcome to ")
    time.sleep(0.1)
    os.system("clear")
    green("Welcome to C")
    time.sleep(0.1)
    os.system("clear")
    green("Welcome to Cy")
    time.sleep(0.1)
    os.system("clear")
    green("Welcome to Cyb")
    time.sleep(0.1)
    os.system("clear")
    green("Welcome to Cyber")
    time.sleep(0.1)
    os.system("clear")
    green("Welcome to CyberT")
    time.sleep(0.1)
    os.system("clear")
    green("Welcome to CyberTi")
    time.sleep(0.1)
    os.system("clear")
    green("Welcome to CyberTim")
    time.sleep(0.1)
    os.system("clear")
    green("Welcome to CyberTime")
    time.sleep(0.1)
    os.system("clear")
    green("Welcome to CyberTime!")
    main_menu()


def main_menu():
    os.system("clear")
    green("Welcome to CyberTime!")
    main_menu = ["play", "settings", "credits", "exit"]
    terminal_main_menu = TerminalMenu(main_menu)
    terminal_main_menu_entry_index = terminal_main_menu.show()
    print(terminal_main_menu_entry_index)
    if terminal_main_menu_entry_index == 0:
        os.system("clear")
        start_game()
    elif terminal_main_menu_entry_index == 1:
        os.system("clear")
        settings_menu()
    elif terminal_main_menu_entry_index == 2:
        credits_menu()
    elif terminal_main_menu_entry_index == 3:
        os.system("clear")
        exit_menu()

def settings_menu():
    settings_menu = ["coming soon", "coming soon", "coming soon", "back to main menu"]
    blue("settings")
    terminal_settings_menu = TerminalMenu(settings_menu)
    terminal_settings_menu_entry_index = terminal_settings_menu.show()
    print(terminal_settings_menu_entry_index)
    if terminal_settings_menu_entry_index == 0:
        os.system("clear")
        print("coming soon")
    elif terminal_settings_menu_entry_index == 1:
        os.system("clear")
        print("coming soon")
    elif terminal_settings_menu_entry_index == 2:
        os.system("clear")
        print("coming soon")
    elif terminal_settings_menu_entry_index == 3:
        os.system("clear")
        main_menu()

def credits_menu():
        os.system("clear")
        cyan("credits : BringDemocracy")
        time.sleep(2)
        print()
        print("press enter to go back to main menu")
        input()
        main_menu()

def exit_menu():
    os.system("clear")
    red("exiting")
    time.sleep(0.2)
    os.system("clear")
    red("exiting.")
    time.sleep(0.2)
    os.system("clear")
    red("exiting..")
    time.sleep(0.2)
    os.system("clear")
    red("exiting...")
    time.sleep(0.2)
    os.system("clear")
    exit()

def start_game():
    os.system("clear")
    yellow("year 2080")
    time.sleep(1)
    yellow("You just immigrated to the United States of America.")
    yellow("You are making your identity card at the mayorship.")
    time.sleep(3)
    os.system("clear")
    green("Hello, what is your name?")
    player.name = input("my name is: ")
    green("Okay, and what is your age?")
    player.age = int(input("I am : "))
    green("So you are " + str(player.age) + " years old and your name is " + player.name + " .")
    green("Is that correct?")
    correct = input("yes or no: ")
    if correct == "yes":
        os.system("clear")
        yellow("You are now a citizen of the United States of America.")
    if correct == "no":
        os.system("clear")
        green("Okay, let's try again.")
        start_game()
    



    


class Player:
    def __init__(self, name, health, attack, money, age):
        self.name = name
        self.health = health
        self.attack = attack
        self.money = money
        self.age = age

player = Player("", 100, 10, 0, 0)




launch()

    
