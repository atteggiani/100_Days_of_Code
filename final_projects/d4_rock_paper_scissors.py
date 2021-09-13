# Program to play rock-paper-scissor game with the computer.
import random

def intro():
    print("Welcome to the rock-paper-scissor game!!")
def rock():
    print('''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    ''')

def paper():
    print('''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    ''')

def scissors():
    print('''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    ''')

def print_choice(ans):
    if ans == 0:
        rock()
    elif ans == 1:
        paper()
    else:
        scissors()

random.seed()
intro()

while True:
    pc = random.randint(0,2)

    print("\nWhat do you choose?")
    while True:
        try:
            ans=int(input("Type 0 for Rock, 1 for Paper, 2 for Scissor\n"))
            if ans not in [0,1,2]: raise ""
            break
        except:
            print("That's not valid!")
            continue
    print("")

    print_choice(ans)
    print("\n\n")
    print("Computer chose:\n")
    print_choice(pc)
    print("\n\n")
    if pc == ans:
        print("That's a tie!")
    elif pc > ans:
        if (pc == 2) and (ans == 0):
            print("YOU WON!!!")
        else:
            print("You lose :(")
    else:
        if (pc == 0) and (ans == 2):
            print("You lose :(")
        else:
            print("YOU WON!!!")

    print("\n\n\n")
    p=input("Type 'p' to play again, type anything else to quit.\n")
    if p == 'p':
        continue
    else:
        exit()


