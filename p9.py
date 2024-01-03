def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32)*5/9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
convert = True
while convert:
    print("1.celsius to fahrenheit")
    print("2.fahrenheit to celsius")
    choice = input("Enter your choice 1/2 ")

    if choice == "1":
        celsius = float(input("Enter temperature in celsius "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} celsius is equals to {fahrenheit} fahrenheit")

    elif choice == "2":
        fahrenheit = float(input("Enter temperature in fahrenheit "))
        celsius  = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} celsius is equals to {celsius} fahrenheit")

    else:
        print("Invalid choice!")
    user_choice = input("do you want to convert again! y/n")
    if user_choice == 'y':
        convert = True
    else:
        convert = False