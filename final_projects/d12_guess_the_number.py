import os
import random 
random.seed()

def clear():
    os.system('cls||clear')

def print_logo():
    clear()
    print("""
       ____                      _   _           
      / ___|_   _  ___ ___ ___  | |_| |__   ___  
     | |  _| | | |/ _ / __/ __| | __| '_ \ / _ \ 
     | |_| | |_| |  __\__ \__ \ | |_| | | |  __/ 
      \____|\__,_|\___|___|___/  \__|_| |_|\___| 
                            _               _    
      _ __  _   _ _ __ ___ | |__   ___ _ __| |   
     | '_ \| | | | '_ ` _ \| '_ \ / _ | '__| |   
     | | | | |_| | | | | | | |_) |  __| |  |_|   
     |_| |_|\__,_|_| |_| |_|_.__/ \___|_|  (_)   
     """)

def check_input(prompt,condition,err_msg):
    while True:
        try:
            ans=input(prompt)
            if not condition(ans): raise ""
            break
        except:
            print(err_msg)
            continue
    return ans

while True:
    print_logo()
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100.!")

    diff=check_input(prompt="Choose a difficulty. Type 'easy' or 'hard': ",
                condition=lambda x: x.strip().lower() in ['easy','hard','e','h'],
                err_msg="Invalid difficulty.").strip().lower()
    if diff in ['easy','e']:
        n=10
    else:
        n=5

    num = random.randint(1,100)
    while n>0:
        print(f"You have {n} attempts remaining to guess the number.")
        guess = int(check_input(prompt="Make a guess: ",
                        condition=lambda x: int(x.strip().isnumeric()) and int(x)<=100 and int(x)>0,
                        err_msg="Insert a valid number between 1 and 100."))
        if guess > num:
            print("Too high.\nGuess again.")
            n-=1
        elif guess < num:
            print("Too low.\nGuess again.")
            n-=1
        else:
            print(f"You got it! The answer was {guess}")
            break
    else:
        print("You've run out of guesses, you lose.")
    r=input("Type 'r' to restart. Type anything else to exit. ")
    if r=='r':
        continue
    else:
        os._exit(0)

