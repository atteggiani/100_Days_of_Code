#!/Applications/anaconda3/bin/python
from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
    '''

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

def flush():
    clear()
    print(logo)
    print("Welcome to the secret auction program.")
    print(f"Number of current total bidders: {nbidders}\n")

bidders = {}
nbidders = 0
while True:
    while True:
        flush()
        name = check_input(
            prompt = "What is your name?: ",
            condition = lambda x: x.strip(),
            err_msg = "Please insert a valid name!")
        if name in bidders:
            count = 2
            newname = name
            while newname in bidders:
                newname = f"{name}_{count}"
                count +=1
            ans=input(f"There is already a bidder named '{name}'. Do you want to be named '{newname}' instead?\n"\
                    "Type 'yes' or 'no' to choose a different name: ")
            if ans.strip().lower() in ['yes','y']:
                name = newname
            else:
                continue
        bid = float(check_input(
            prompt = "What is your bid?: $",
            condition = lambda x: float(x),
            err_msg = "Please insert a valid number!"))
        bidders.update({name:bid})
        nbidders +=1
        morebids=input("\nAre there any other bidders? Type 'yes' or 'no': ")
        if morebids.strip().lower() in ["yes","y"]:
            continue
        else:
            break
    break
flush()
winner = [n for n in bidders if bidders[n] == max(bidders.values())]
if len(winner)==1:
    winner = winner[0]
    print(f"The winner is {winner} with a bid of ${bidders[winner]}!\n")
else:
    while len(winner) > 1:
        val=bidders[winner[0]]
        print(f"There is a tie between {', '.join(winner[:-1])} and {winner[-1]} with a bid of ${val}.\n")
        print("There will be another secret bid within them to declare the final winner.\n")
        for w in winner:
            tiebreak = check_input(
                    prompt = f"{w} please type 'ok' when you are ready... ",
                    condition = lambda x: x.strip().lower() in ['ok','o'],
                    err_msg = "")
            bid = float(check_input(
                prompt = f"{w} what is your bid? (Should be higher than your last one): $",
                condition = lambda x: float(x) > bidders[w],
                err_msg = "Please insert a valid number, higher than your last bid!"))
            bidders.update({w:bid}) 
            flush()  
            print(f"There is a tie between {', '.join(winner[:-1])} and {winner[-1]} with a bid of ${val}.\n")
            print("There will be another secret bid within them to declare the final winner.\n")
        winner = [n for n in bidders if bidders[n] == max(bidders.values())]
        if len(winner)==1:
            flush()
            winner = winner[0]
            print(f"The winner is {winner} with a bid of ${bidders[winner]}!\n")
        else:
            continue