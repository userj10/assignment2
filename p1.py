import random
def play():
    chances = 5
    score = 0
    number = random.randint(1, 100)
    is_game_on = True
    while is_game_on:
        if chances == 0:
            print("you lost")
            is_game_on = False
            break
        guess = int(input("guess the number"))
        if guess < number:
            print("your guess is too low")
            chances -= 1
            print(f"you have {chances} attempts remaining")
        elif guess > number:
            print("your guess is too high")
            chances -= 1
            print(f"you have {chances} attempts remaining")
        elif guess == number:
            print("you have guessed a correct number")
            is_game_on = False
            score += 1
    print(f"your score is {score}")

play()
user_choice = input("do you want to play again y/n").lower()
if user_choice == "y":
    play()