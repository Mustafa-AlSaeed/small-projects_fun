import random

def my_roll(sides = 6):
    roll = random.randint(1,6)
    return roll

def diceroll():
    rolling = True
    while rolling:
        roll_1a = input('Ready to roll? press ENTER to roll, or q to quit')

        if roll_1a != 'q':
            num_rolled = my_roll()
            print("you rolled ", num_rolled)
        else:
            rolling = False
    print ("thanks for playing")


diceroll()
