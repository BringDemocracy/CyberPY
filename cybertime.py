from colorist import red, green, blue, yellow, magenta, cyan, white
import time
import random
import os
from simple_term_menu import TerminalMenu

def launch():
    os.system("clear")
    welcome_message = "Welcomet to CyberPY!"
    for i in range(len(welcome_message)):
        time.sleep(0.1)
        os.system("clear")
        green(welcome_message[:i+1])
    main_menu()


def main_menu():
    os.system("clear")
    green("Welcome to CyberPY!")
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
    message_1 = "year 2080"
    for i in range(len(message_1)):
        time.sleep(0.1)
        os.system("clear")
        yellow(message_1[:i+1])
    time.sleep(1)
    message_2 = "You just immigrated to the United States of America."
    for i in range(len(message_2)):
        time.sleep(0.1)
        os.system("clear")
        yellow(message_2[:i+1])
    time.sleep(1)
    message_3 = "You are now at the mayorship, making your identity card."
    for i in range(len(message_3)):
        time.sleep(0.1)
        os.system("clear")
        yellow(message_3[:i+1])
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
        message_4 = "You are now a citizen of the United States of America."
        for i in range(len(message_4)):
            time.sleep(0.1)
            os.system("clear")
            yellow(message_4[:i+1])
        time.sleep(1)
        message_5 = "You're going in the city to find a job"
        for i in range(len(message_5)):
            time.sleep(0.1)
            os.system("clear")
            yellow(message_5[:i+1])
            time.sleep(1)
        
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

    
