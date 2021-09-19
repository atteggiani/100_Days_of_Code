logo = """             _           _     _     _
            | |         | |   | |   (_)
,--------.  | |__  _   _| |__ | |__  _
|        |  | '_ \| | | | '_ \| '_ \| |
|A _  _  |  | |_) | |_| | |_) | |_) | |
| ( \/ ) |  |_.__/ \___/|_.__/|_.__/|_|
|  \  /  |-----.    _     _            _    _            _    
|   \/ A |     |   | |   | |          | |  (_)          | |   
|        |/\   |   | |__ | | __ _  ___| | ___  __ _  ___| | __
`--------'  \  |   | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
      |  \  /  |   | |_) | | (_| | (__|   <| | (_| | (__|   < 
      |   \/ K |   |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |        |                          _/ |                
      `--------'                         |__/           
"""

def print_cards(cards,hidden=False):
      n = len(cards)
      if n == 0:
            print("\n"*4)
      else:
            s1=""
            s2=""
            if hidden and len(cards) == 2:
                  cards[1] = ' ?'
            for card in cards:
                  val = card[:-1]
                  color = card[-1]
                  N = val
                  s = "" if len(val) == 2 else " "
                  if color == 'H':
                        C = "\u2665"
                  elif color == 'D':
                        C = "\u2666"
                  elif color == 'S':
                        C = "\u2660"
                  elif color == 'C':
                        C = "\u2663"
                  elif color == '?':
                        C = "?"
                        s = "?"
                  s1+=f"|{N}{C}{s} |"
                  s2+=f"| {C}{C} |"
            print(",----."*n)
            print(s1)
            print(s2)
            print(s2)
            print("`----'"*n)
