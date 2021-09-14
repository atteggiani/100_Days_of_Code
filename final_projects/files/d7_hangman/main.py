#!/Applications/anaconda3/bin/python
# Program to play the famous game Hangman
from replit import clear
from arts import *
from word_list import *
import random

def flush():
    clear()
    print(logo,end="\n\n")

def check_input():
    while True:
        try:
            letter=input("Guess a letter: ")
            if not (letter.isalpha() and len(letter)==1): raise ""
            break
        except:
            print(f"{letter} is not a valid letter.\n")
            continue
    return letter.lower()

def print_guessed_word():
    spaced_guessed_word = " ".join(guessed_word)
    print(f"Your word: {spaced_guessed_word}\n")

def change_guessed_word():
    return [letter if c1 == letter else c2 for c1,c2 in zip(word,guessed_word)]

def print_stages():
    print(stages[lives])

def print_lives():
    print(f"Number of lives left: {lives}\n")

def flow():
    print_stages()
    print_lives()
    print_guessed_word()

def life_lost():
    flush()
    print(f"You guessed {letter}, that's NOT in the word. You lost a life!")
    flow()

def letter_guessed():
    flush()
    print(f"You guessed {letter}, that IS in the word!!")
    flow()

def replay():
    ans=input("Type 'p' to play again, type anything else to exit. ")
    try:
        if not ans.lower() == 'p':
            exit()
    except:
        exit()

def death():
    print("YOU DIED!\n")
    print(death_logo)
    replay()

def win():
    print("You won!! Congratulations!\n")
    print(win_logo)
    replay()

random.seed()
while True:
    flush()
    print("")    
    lives = len(stages)-1
    word = random.choice(word_list)
    guessed_word = ["_" for _ in range(len(word))]
    flow()
    while lives:
            letter=check_input()
            if letter not in word:
                lives-=1
                life_lost()
            else:
                guessed_word = change_guessed_word()
                if "_" in guessed_word:
                    letter_guessed()
                else:
                    letter_guessed()
                    win()
                    break
    else:
        death()
    continue


