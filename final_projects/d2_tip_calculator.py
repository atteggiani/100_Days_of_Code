print("Welcome to the tip calculator.")
tot=float(input("What was the total bill? $"))
tip=float(input("What percentage tip would you like to give? (type 0 for no tip, for the sadness of waiters) "))
num=int(input("How many people to split the bill? "))

split= round((tot+tip*tot/100)/num,2)

print(f"Each person should pay: ${split}")