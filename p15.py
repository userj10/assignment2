
shopping_list = ['Milk', 'Bread', 'curd', 'Onion']
print(shopping_list)

def add_items():
    items = eval(input("Enter the list of items you want to add "))
    shopping_list.extend(items)

def remove_item():
    item = input("enter the item which you want to remove ")
    shopping_list.remove(item)
modify = True
while modify:
    print("1.add items to list")
    print("2.remove items from list")
    user_choice = input("enter your choice ")
    if user_choice == '1':
        add_items()
        print(shopping_list)
    elif user_choice == '2':
        remove_item()
        print(shopping_list)
    choice = input("Do you want to modify y/n").lower()
    if choice == 'y':
        modify = True
    else:
        modify = False
