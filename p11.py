def guess_a_number():
    user_number = int(input("choose a number between 1 to 100 "))
    low = 1
    high = 100

    while True:
        guess = (low + high )// 2
        response = input(f"Is your number {guess}?? yes/no ")

        if response == 'yes':
            print("you guessed a correct number ")
            break
        elif response == 'no':
            hint = input("Is my guess is lower or higher than your number lower/higher")

            if hint == 'lower':
                low = guess + 1
            elif hint == 'higher':
                high = guess - 1
            else:
                print("please enter a input as lower or higher ")
        else:
            print("Invalid response")
guess_a_number()