def remove_all_even_numbers():
    my_list = [1,2,3,4,5,6,7,8,9]
    new_list = []
    for number in my_list:
        if number % 2 != 0:
            new_list.append(number)
    print(new_list)

def remove_elements_shorter_than_5_characters():
    my_list = ["apple", "banana", "kiwi", "grape", "pear", "orange"]
    new_list = []
    for element in my_list:
        if len(element) >= 5:
            new_list.append(element)
    print(new_list)

print("1.remove all even numbers from a list")
print("2.remove elements shorter than 5 characters ")
choice = input("enter your choice ")

if choice == '1':
    remove_all_even_numbers()
elif choice == '2':
    remove_elements_shorter_than_5_characters()
else:
    print("invalid input")