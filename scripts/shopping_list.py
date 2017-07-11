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
show_help()

while True:
    # ask for new items
    new_item = input("> ")

    # allow for quiting app
    if new_item == 'DONE':
         break

    # add new items to the list
    shopping_list.append(new_item)

# print out the list
print("Here's your list:")
for item in shopping_list:
    print(item)
