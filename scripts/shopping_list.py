# Author: Johnny Romano
# make a list app to hold onto items
shopping_list = []

# print out instructions on how to use the app
def show_help():
    print("\nWhat do we need to get while we're out?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
""")

def show_list():
    # print out the list
    print("\nHere's your list:")
    for item in shopping_list:
        print(item)

def add_to_list(new_item):
    # add new items to the list
    shopping_list.append(new_item)

def main():
    show_help()
    while True:
        # ask for new items
        new_item = input("> ")

        # allow for quiting app
        if new_item == 'DONE':
            print("\nList has {} items.".format(len(shopping_list)))
            break
        # or ask for help
        elif new_item == 'HELP':
            show_help()
            continue
        elif new_item == 'SHOW':
            show_list()
            continue
        add_to_list(new_item)

    show_list()

main()
