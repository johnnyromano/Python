# make a list to hold onto items
shopping_list = []

# print out instructions on how to use the app
print("What do we need to get while we're out?")
print("Enter 'DONE' to stop adding items.")

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
