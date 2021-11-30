from os import system, name
from day_9_art import logo


def clear():
    system('clear')


# print(logo)

name_list = {}

def add_name():
    key = input("Name? ")
    value = int(input("Value? "))
    name_list[key] = value


add_name()
loop = True
while loop:
    more = input("Any other? ")
    if more == 'y':
        clear()
        add_name()
    elif more == 'n':
        loop = False
        # max = max(name_list[])
        print(name_list)

