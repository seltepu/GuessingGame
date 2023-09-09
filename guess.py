import random

def number_generator():
    min = 0
    max = 100
    random_num = random.randint(min,max)
    return random_num



def guesser():
    while True:
        player_guess = input("Guess a number between 1 and 100:    ")
        if player_guess.isdigit():
            player_guess = int(player_guess)
            if 1 < player_guess < 100:
                break
            else:
                print("Number must be between 1 and 100!")
        else:
            print("Invalid. Input a number!")
    
    value = number_generator()
    while player_guess !=value:
        if player_guess<value:
            print("Guess a larger number!")
                
        else:
            print("Guess a smaller number!")
        player_guess = int(input("Guess again:  "))

        if player_guess == value:
            print(f"Congrats! You have guessed the number! It was {value}!")

guesser()

