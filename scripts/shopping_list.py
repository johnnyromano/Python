#!/usr/bin/env python
"""
    File name: shopping_list.py
    Description: Make a list app to hold onto items
    Author: Johnny Romano
    Email: John.p.romano@gmail.com
    Date created: 11-July-2017
    Date last modified: 19-July-2017
    Python Version: 3.5
"""
import os

shopping_list = []

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# print out instructions on how to use the app
def show_help():
    clear_screen()
    print("\nWhat do we need to get while we're out?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
Enter 'REMOVE' to delete an item from your list.
""")

def add_to_list(item):
    # add new items to the list
    show_list()
    if len(shopping_list):
        position = input("Where should I add {}?\n"
                         "Enter # or Press ENTER to add to the end of the list...\n"
                         "> ".format(item))
    else:
        position = 0

    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        shopping_list.append(item)
    show_list()

def show_list():
    clear_screen()
    # print out the list
    print("\nHere's your list:")

    index = 1
    for item in shopping_list:
        print("{}. {}".format(index,item))
        index += 1

    print("-"*10)

def remove_from_list():
    show_list()
    what_to_remove = input("What would you like to remove?\n> ")
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass
    show_list()

def main():
    show_help()
    while True:
        # ask for new items
        new_item = input("> ")

        # allow for quiting app
        if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
            print("\nList has {} items.".format(len(shopping_list)))
            break
        # or ask for help
        elif new_item.upper() == 'HELP':
            show_help()
            continue
        elif new_item.upper() == 'SHOW':
            show_list()
            continue
        elif new_item.upper() == 'REMOVE':
            remove_from_list()
        else:
            add_to_list(new_item)

    show_list()

main()
