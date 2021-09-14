#!/Applications/anaconda3/bin/python
import random

def check_input(prompt,condition,err_msg):
    while True:
        try:
            ans=input(prompt)
            if not condition(ans): raise ""
            break
        except:
            print(err_msg,end="")
            continue
    return ans

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!\n")
nlett = int(check_input(prompt = "How many letters would you like in your password?\n",
            condition = lambda x: int(x),
            err_msg = "That's not a valid number!\n"))
nsymb = int(check_input(prompt = "How many symbols would you like?\n",
            condition = lambda x: int(x),
            err_msg = "That's not a valid number!\n"))            
nnumb = int(check_input(prompt = "How many numbers would you like?\n",
            condition = lambda x: int(x),
            err_msg = "That's not a valid number!\n"))

random.seed()
psw=""
for _ in range(nlett):
    psw+=random.choice(letters)
for _ in range(nsymb):
    psw+=random.choice(symbols)
for _ in range(nnumb):
    psw+=random.choice(numbers)

newpsw=''.join(random.sample(psw,len(psw)))   
print(f"Your password is: {newpsw}")