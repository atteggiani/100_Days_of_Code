#!/Applications/anaconda3/bin/python
from replit import clear

logo = """           
     ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
    a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
    8b         ,adPPPPP88 8PP"'"'"'" `"Y8ba,   ,adPPPPP88 88
    "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
     `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
                                                               
               88             88                                 
               ""             88                                 
     ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
    8b         88 88       d8 88       88 8PP"'"'"'" 88          
    "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
     `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                  88                                             
                  88           
    """

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

def main_operation(msg,key,encription=True):
    from string import ascii_lowercase as alphabet_low
    from string import ascii_uppercase as alphabet_up
    if encription:
        fun_low = lambda ch: alphabet_low[(alphabet_low.index(ch) + key)%len(alphabet_low)]
        fun_up = lambda ch: alphabet_up[(alphabet_up.index(ch) + key)%len(alphabet_up)]
    else:
        fun_low = lambda ch: alphabet_low[(alphabet_low.index(ch) - key)%len(alphabet_low)]
        fun_up = lambda ch: alphabet_up[(alphabet_up.index(ch) - key)%len(alphabet_up)]
    
    new_msg=""
    for ch in msg:
        if ch in alphabet_low:
            newch=fun_low(ch)
        elif ch in alphabet_up:
            newch=fun_up(ch)
        else:
            newch=ch
        new_msg+=newch
    return new_msg

clear()
print(logo)
while True:
    operation = check_input(
        prompt = "Type 'encode' to encript, type 'decode' to decript:\n",
        condition = lambda x: x.lower() in ['encode','e','decode','d'],
        err_msg = "That input is not valid!\n").lower()
    message = input("\nType your message:\n")
    key = int(check_input(
            prompt = "\nType key number:\n",
            condition = lambda x: x.isdigit(),
            err_msg = "Please type a valid integer number!"))
    if operation in ["encode","e"]:
        w = "encoded"
        f = encription = True
    else:
        w = "decoded"
        f = encription = False
    print(f"\nHere's the {w} message:\n{main_operation(message,key,encription)}\n")
    replay = input("Type 'y' to to keep encoding/decoding messages. Type anything else to exit. ")
    if replay == 'y':
        print("")
        continue
    else:
        exit()
