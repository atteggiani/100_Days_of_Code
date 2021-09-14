#!/Applications/anaconda3/bin/python
# Program to play the famous game Hangman
from arts import *
from word_list import *
import random

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

def separation():
    print("\n")
    print("==================================")
    print("\n")

def print_guessed_word():
    spaced_guessed_word = " ".join(guessed_word)
    print(f"Your word: {spaced_guessed_word}")

def change_guessed_word():
    return [letter if c1 == letter else c2 for c1,c2 in zip(word,guessed_word)]

def print_stages():
    print(stages[lives])

def print_lives():
    print(f"Number of lives left: {lives}")

def flow():
    print_guessed_word()
    print_stages()
    print_lives()
    separation()

def life_lost():
    print(f"You guessed {letter}, that's NOT in the word. You lost a life!\n")
    flow()

def letter_guessed():
    print(f"You guessed {letter}, that IS in the word!!\n")
    flow()

def replay():
    ans=input("Type 'p' to play again, type anything else to exit. ")
    try:
        if not ans.lower() == 'p':
            exit()
        print("")
        print("========================================")
        print("========================================")
        print("========================================")
        print("\n")
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
print(logo,end="\n\n\n")

while True:
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


