#!/Users/dmar0022/university/udemy/100_Days_of_Code/final_projects/files/d11_blackjack/env_bubbi_blackjack/bin/python
import arts 
from colorama import Fore, Back, Style
import random
import time
import re

class Player():
    def __init__(self,name = None, hidden = False, colour=None):
        self.cards = {'s1':[]}
        self.value = {'s1':[0]}
        self.bet = {'s1':0}
        self.position = 0
        self.name = name
        self.hidden = hidden
        self.status = {'s1':None}
        self.colour = colour
        self.colourstring = self.compute_colourstring()
        self.colourname = self.compute_colourname()
        self.nslots = 1

    def split(self,slot):
        self.add_slot()
        slotin = slot
        slotend = self.nslots
        self.bet[f's{slotend}'] = self.bet[f's{slotin}']
        card=self.cards[f's{slotin}'].pop(1)
        self._add_card(card,slot=slotend)
        print_cards()
        self.deal(slot=slotin)
        
    def add_slot(self):
        self.nslots += 1
        slotstr=f"s{self.nslots}"
        self.cards[slotstr] = []
        self.value[slotstr] = [0]
        self.bet[slotstr] = 0
        self.status[slotstr] = None

    def can_split(self,slot=1):
        s = f's{slot}'
        if len(self.cards[s]) == 2:
            arr=['10','J','Q','K']
            val = [c[:-1] for c in self.cards[s]]
            if (val[0] == val[1]) or (val[0] in arr and val[1] in arr):
                return True
        return False

    def has_busted(self,slot=1):
        s = f's{slot}'
        return 

    def update_status(self,status=None,slot=1):
        self.compute_value()
        s = f's{slot}'  
        current = self.status[s]
        if current is not None:
            raise Exception(f"Slot {slot}'s Status is already set to '{current}', and cannot be updated anymore.")
        if status is None:
            if max(self.value[s]) == 21:
                self.status[s] = 'BLACKJACK'
                self.value[s] = [21]
            elif self.value[s][0] > 21: 
                self.status[s] = 'BUSTED'
        else:
            self.status[s] = status

    def _add_card(self,card,slot):
        self.cards[f's{slot}'].append(card)
        self.update_status(slot=slot)

    def compute_value(self): 
        val = {s:[0] for s in self.cards}
        for s,cards in self.cards.items():
            if self.ishidden() and len(cards) ==2:
                cards = cards[:-1].copy()
            for card in cards:
                card = card[:-1]
                try:
                    val[s] = [v + int(card) for v in val[s]]
                except ValueError:
                    if card == 'A':
                        val[s] = [val[s][0]+1,val[s][0]+11]
                    else:
                        val[s] = [v + 10 for v in val[s]]                
                try:
                    if val[s][1] > 21: del val[s][1]
                except:
                    pass
            self.value[s] = val[s]
            if self.status[s] == 'BLACKJACK':
                self.value[s] = [21]
            elif self.status[s] == 'STAND':
                self.value[s] = [max(self.value[s])]

    def compute_colourstring(self):
        if self.colour is not None:
            return f"{self.colour['Fore']}{self.colour['Back']}"
        else:
            return ""

    def compute_colourname(self):
        return f"{self.colourstring}{self.name}{Style.RESET_ALL}"

    def deal(self,wait=0.5,slot=1):
        if wait is not None:
            time.sleep(wait)
        self._add_card(shoe.pop(),slot=slot)
        print_cards()
    
    def ishidden(self):
        return self.hidden
    
    def reveal(self):
        if self.ishidden():
            self.hidden = False
            self.update_status()
        else:
            raise Exception("Can't reveal a non-hidden player")

    def reset(self,hidden=False):
        self.cards = {'s1':[]}
        self.value = {'s1':[0]}
        self.bet = {'s1':0}
        self.hidden = hidden
        self.status = {'s1':None}
        self.nslots = 1

def print_cards():
    flush()
    # PLAYERS
    for p in players: 
        print(p.colourname)
        for s,value in p.value.items():
            if int(s[1:]) > 1:
                print("-"*28) 
            print(f"Bet: ${p.bet[s]:.2f}")
            arts.print_cards(p.cards[s])
            if len(value) == 1:
                print(f"Hand: {value[0]}",end="")            
            else:
                print(f"Hand: {value[0]} / {value[1]}",end="")
            if p.status[s] is None:
                print("")
            else:
                print(f" {p.status[s]}")
        print("-"*150)   
    # DEALER
    print(pc.colourname)
    arts.print_cards(pc.cards['s1'].copy(),pc.hidden)
    if len(pc.value['s1']) == 1:
        print(f"Hand: {pc.value['s1'][0]}",end="")            
    else:
        print(f"Hand: {pc.value['s1'][0]} / {pc.value['s1'][1]}",end="")
    if pc.status['s1'] is None:
        print("")
    else:
        print(f" {pc.status['s1']}")
    print("")

def clear():
    import os
    os.system('cls||clear')

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

colours = {'Fore':[
                Fore.LIGHTRED_EX,Fore.LIGHTGREEN_EX,Fore.LIGHTCYAN_EX,
                Fore.LIGHTYELLOW_EX,Fore.LIGHTMAGENTA_EX,Fore.LIGHTBLUE_EX,
                Fore.LIGHTWHITE_EX,Fore.GREEN,Fore.RED],
            'Back':[Back.BLACK]*9}

# Initialize cards, deck and shoe (based on number of decsk)
tot_cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
card_colors = ["H","D","C","S"]
deck = [f"{val}{c}" for c in card_colors for val in tot_cards]
ndecks = 10
shoe_base = deck * ndecks

# Clear screen and print logo
clear()
print(arts.logo)
max_players = 9
# Define number of players and names (currently only 1 player supported)
nplayers = int(check_input(
    prompt=f"How many players? (max {max_players}) ",
    condition=lambda x: int(x) <= max_players and int(x) > 0,
    err_msg=f"Please enter a valid number of players (max {max_players})"))
players=[]    
for i in range(nplayers):
    while True:
        name = check_input(
            prompt=f"{colours['Fore'][i]}{colours['Back'][i]}Player {i+1}{Style.RESET_ALL}, what is your name?\n",
            condition=lambda x: bool(re.match("^[a-zA-Z0-9!@#\$%\^\&*\)\(+=._-]{1,15}$",x.strip())),
            err_msg="Your name can have max 15 characters among letters, numbers and the following special characters: .!@#$%^&_+-=*()\n").strip()
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

# ==================================================================================================
# ==================================================================================================
# START
while True:
    shoe = shuffle()
    flush()
    # Define bets
    for p in players:
        bet = float(check_input(
            prompt=f"{p.colourname}, how much do you want to bet? $",
            condition=lambda x: float(x) > 0,
            err_msg="Please insert a valid number!"))
        p.bet['s1'] = bet
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
        restart = True
        while restart:
            for s in p.cards.copy():
                restart = False
                slot=int(s[1:])
                if len(p.cards[s]) == 1: p.deal(slot=slot)
                while True:
                    if p.status[s] in ['BLACKJACK','BUSTED','STAND']:
                        break
                    print(f"It's {p.colourname}'s turn. What do you want to do?")
                    #If player has 2 cards: enable DOUBLE DOWN and SPLIT
                    if len(p.cards[s]) == 2:
                        if p.can_split(slot):
                            prompt="Type 'h' for HIT, 's' for STAND, 'dd' for DOUBLE DOWN, 'split' for SPLIT\n"
                            condition=lambda x: x.strip().lower() in ['h','s','dd','hit','stand','double down', 'doubledown','split']
                        else:
                            prompt="Type 'h' for HIT, 's' for STAND, 'dd' for DOUBLE DOWN\n"
                            condition=lambda x: x.strip().lower() in ['h','s','dd','hit','stand','double down', 'doubledown']
                    # Otherwise only HIT or STAND possible
                    else:
                        prompt="Type 'h' for HIT, 's' for STAND\n"
                        condition=lambda x: x.strip().lower() in ['h','s','hit','stand']
                    action = check_input(
                        prompt=prompt,
                        condition=condition,
                        err_msg="Action not valid.").strip().lower()
                    # Do respective actions 
                    if action in ['h','hit']:
                        p.deal(slot=slot)
                        continue
                    elif action in ['s','stand']:
                        p.update_status("STAND",slot=slot)
                        print_cards()
                        break
                    elif action in ['dd','double down', 'doubledown']:
                        p.bet[s] *= 2
                        p.deal(slot=slot)
                        if p.status[s] is None:
                            p.update_status("STAND",slot=slot)
                            print_cards()
                        break
                    elif action == 'split':
                        p.split(slot=slot)
                        restart = True
                if restart:
                    break

    # # Dealer's turn:
    time.sleep(1)
    pc.reveal()
    print_cards()
    print(f"DEALER reveals a {pc.cards['s1'][-1][:-1]}")
    time.sleep(1)
    while max(pc.value['s1']) < 17:
        pc.deal(wait=1)
    if pc.status['s1'] is None:
        pc.update_status('STAND')
        print_cards()
    time.sleep(.5)

    # RESULTS
    paystring=""
    for p in players:
        for s in p.cards:
            if p.status[s] == "BLACKJACK":
                if pc.status['s1'] != "BLACKJACK":
                    payout = 1.5*p.bet[s]
                    paystring += f"{p.colourname} did BLACKJACK and won {payout:.2f}$!!\n"
                    p.position += payout
                else:
                    paystring += f"{p.colourname} PUSHED\n"
            elif p.status[s] == "BUSTED":
                payout = p.bet[s]
                p.position -= payout
                paystring += f"{p.colourname} BUSTED and lost {payout:.2f}$\n"
            elif (p.value[s] > pc.value['s1']) or (p.value[s] < pc.value['s1'] and pc.status['s1'] == "BUSTED"):
                payout = p.bet[s]
                p.position += payout
                paystring += f"{p.colourname} won {payout:.2f}$\n"
            elif p.value[s] < pc.value['s1']:
                    payout = p.bet[s]
                    p.position -= payout
                    paystring += f"{p.colourname} lost {payout:.2f}$\n"
            elif p.value[s] == pc.value['s1']:
                paystring += f"{p.colourname} PUSHED\n"
    print_cards()
    print(paystring)
    for p in players:
        p.reset()
    pc.reset(hidden=True)
    input("Type any key to continue... ")