#!/Applications/anaconda3/bin/python
import arts 
import random
import time
from itertools import compress
import numpy as np
from colorama import Fore, Back, Style

def clear():
    import os
    os.system('cls||clear')

class Player():
    def __init__(self,name = None, hidden = False, colour=None):
        self.cards = []
        self.value = [0]
        self.bet = 0
        self.position = 0
        self.name = name
        self.hidden = hidden
        self.status = None
        self.colour = colour
        self.colourstring = self.compute_colourstring()
        self.colourname = self.compute_colourname()
        # self.nslots = 1

    def has_busted(self):
        return self.value[0] > 21

    def update_status(self,status=None):
        if self.status is not None:
                raise Exception(f"Status is already set to '{self.status}', and cannot be updated anymore.")
        if status is None:
            if self.has_blackjack(): 
                self.status = 'BLACKJACK'
            elif self.has_busted(): 
                self.status = 'BUSTED'
        else:
            self.status = status
        self.compute_value()

    def has_blackjack(self):
        if len(self.value) == 1:
            return self.value[0] == 21
        else:
            return self.value[1] == 21
    
    def _add_card(self,card):
        self.cards.append(card)
        self.compute_value()
        self.update_status()

    def compute_value(self): 
        if self.ishidden() and len(self.cards) ==2:
            cards = self.cards[:-1].copy()
        else:
            cards = self.cards
        val = [0]
        for card in cards:
            card = card[:-1]
            try:
                val = [v + int(card) for v in val]
            except ValueError:
                if card == 'A':
                    val = [val[0]+1,val[0]+11]
                else:
                    val = [v + 10 for v in val]                
            try:
                if val[1] > 21: del val[1]
            except:
                pass
        self.value = val
        if self.has_blackjack():
            self.value = [21]
        elif self.status == 'STAND':
            self.value = [max(self.value)]

    def compute_colourstring(self):
        if self.colour is not None:
            return f"{self.colour['Fore']}{self.colour['Back']}"
        else:
            return ""

    def compute_colourname(self):
        return f"{self.colourstring}{self.name}{Style.RESET_ALL}"

    def deal(self,wait=0.5):
        if wait is not None:
            time.sleep(wait)
        self._add_card(shoe.pop())
        print_cards()
    
    def ishidden(self):
        return self.hidden
    
    def reveal(self):
        if self.ishidden():
            self.hidden = False
        else:
            raise Exception("Can't reveal a non-hidden player")

    def reset(self,hidden=False):
        self.cards = []
        self.bet = 0
        self.value = [0]
        self.hidden = hidden
        self.status = None

def print_cards():
    flush()
    # PLAYERS
    for p in players:   
        print(p.colourname)
        print(f"Bet: ${p.bet:.2f}")
        arts.print_cards(p.cards)
        if len(p.value) == 1:
            print(f"Hand: {p.value[0]}",end="")            
        else:
            print(f"Hand: {p.value[0]} / {p.value[1]}",end="")
        if p.status is None:
            print("")
        else:
            print(f" {p.status}")
        print("-"*150)   
    # DEALER
    print(pc.colourname)
    arts.print_cards(pc.cards.copy(),pc.hidden)
    if len(pc.value) == 1:
        print(f"Hand: {pc.value[0]}",end="")            
    else:
        print(f"Hand: {pc.value[0]} / {pc.value[1]}",end="")
    if pc.status is None:
        print("")
    else:
        print(f" {pc.status}")
    print("")

def flush():
    clear()
    print(arts.logo)
    str = [f"{p.colourname}: {p.position:+.2f}$" for p in players]
    print(" | ".join(str))
    print("="*150)
    print("")

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

def shuffle():
    shoe = shoe_base.copy()
    random.shuffle(shoe)
    return shoe

colours = {'Fore':[Fore.RED,Fore.GREEN,Fore.CYAN,Fore.YELLOW,Fore.MAGENTA],
          'Back':[Back.BLACK]*5}

# Initialize cards, deck and shoe (based on number of decsk)
tot_cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
card_colors = ["H","D","C","S"]
deck = [f"{val}{c}" for c in card_colors for val in tot_cards]
ndecks = 10
shoe_base = deck * ndecks

# Clear screen and print logo
clear()
print(arts.logo)

# Define number of players and names (currently only 1 player supported)
nplayers = int(check_input(
    prompt="How many players? (max 5) ",
    condition=lambda x: int(x) <=5 and int(x) > 0,
    err_msg="Please enter a valid number of players (max 5)"))
players=[]    
for i in range(nplayers):
    while True:
        name = check_input(
            prompt=f"{colours['Fore'][i]}{colours['Back'][i]}Player {i+1}{Style.RESET_ALL}, what is your name?\n",
            condition=lambda x: x.strip(),
            err_msg="Please enter a valid name.").strip()
        all_names = [p.name for p in players]
        if name in all_names:
            print(f"{name} has already been chosen, please select a different name.")
            continue
        else:
            break
    players.append(Player(
                    name = name,
                    colour={'Fore':colours['Fore'][i],
                            'Back':colours['Back'][i]}))
    print("")
pc = Player(name = 'DEALER',hidden = True,
    colour={'Fore':Fore.BLACK,'Back':Back.WHITE})

# START
# Shuffle shoe
while True:
    shoe = shuffle()
    flush()
    # Define bets
    for p in players:
        bet = float(check_input(
            prompt=f"{p.colourname}, how much do you want to bet? $",
            condition=lambda x: float(x) > 0,
            err_msg="Please insert a valid number!"))
        p.bet = bet
    flush()
    print_cards()
    # Deal first card
    for p in players:
        p.deal()
    pc.deal()
    # Deal second card
    for p in players:
        p.deal()
    pc.deal()

    # # Players' turn:
    for p in players:
        while True:
            if p.status in ['BLACKJACK','BUSTED']:
                break
            print(f"It's {p.colourname}'s turn. What do you want to do?")
            if len(p.cards) == 2:
                action = check_input(
                    prompt="Type 'h' for HIT, 's' for STAND, 'dd' for DOUBLE DOWN\n",
                    condition=lambda x: x.strip().lower() in ['h','s','dd','hit','stand','double down', 'doubledown'],
                    err_msg="Action not valid.").strip().lower()
            else:
                action = check_input(
                    prompt="Type 'h' for HIT, 's' for STAND\n",
                    condition=lambda x: x.strip().lower() in ['h','s','hit','stand'],
                    err_msg="Action not valid.").strip().lower()
            if action in ['h','hit']:
                p.deal()
                continue
            elif action in ['s','stand']:
                p.update_status("STAND")
                print_cards()
                break
            elif action in ['dd','double down', 'doubledown']:
                p.bet *= 2
                p.deal()
                if p.status is None:
                    p.update_status("STAND")
                    print_cards()
                break

    # # Dealer's turn:
    time.sleep(1)
    pc.reveal()
    pc.compute_value()
    print_cards()
    print(f"DEALER reveals a {pc.cards[-1][:-1]}")
    time.sleep(1)
    while max(pc.value) < 17:
        pc.deal()
    time.sleep(1)

    # RESULTS
    paystring=""
    for p in players:
        if p.status == "BLACKJACK":
            if pc.status != "BLACKJACK":
                payout = 1.5*p.bet
                paystring += f"{p.colourname} did BLACKJACK and won {payout:.2f}$!!\n"
                p.position += payout
            else:
                paystring += f"{p.colourname} PUSHED\n"
        elif p.status == "BUSTED":
            payout = p.bet
            p.position -= payout
            paystring += f"{p.colourname} BUSTED and lost {payout:.2f}$\n"
        elif p.value > pc.value:
            payout = p.bet
            p.position += payout
            paystring += f"{p.colourname} won {payout:.2f}$\n"
        elif p.value < pc.value:
            payout = p.bet
            p.position -= payout
            paystring += f"{p.colourname} lost {payout:.2f}$\n"
        elif p.value == pc.value:
            paystring += f"{p.colourname} PUSHED\n"
    print_cards()
    print(paystring)
    for p in players:
        p.reset()
    pc.reset(hidden=True)
    input("Type any key to continue... ")
    continue









