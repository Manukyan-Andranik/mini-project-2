import random
import os

def dice_roll():                             #  Dice roll function
    dice1 = random.randint(a=1, b=6)
    dice2 = random.randint(a=1, b=6)
    summ = dice1 + dice2
    return (dice1, dice2, summ)


start = True

while start:
    os.system("clear")                          # Clear screen

    print("Start Game".center(30," "), end = "\n" * 2)

    dice1, dice2, summ = dice_roll()    # First dice roll

    if not  summ in [4, 5, 6, 8, 9, 10]: 
        print(f"The sum of dice is {dice1} + {dice2} = f{summ}")
        win = summ in [7, 11]
        message = "You win" * win + (not win) * "Wou lost"

    else:
        goal = summ
        print(f"The sum of dice is {dice1} + {dice2} = {summ}")
        print(f"Now your goal number is {goal}")
        
        dice1, dice2, summ = dice_roll()

        while summ != goal and summ != 7:
            dice1, dice2, summ = dice_roll()     
            print(f"The sum of dice is {dice1} + {dice2} = {summ}")
        
        message = "You win" * (summ == goal) + "You lost" * (summ == 7)

    print(message) 
    inp = ""
    while inp not in ["y", "n"]: 
        inp = input("Play again?(Y/n): ").lower()

    start = inp == "y"