class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "5 cent": 0.05,
        "10 cent": 0.10,
        "20 cent": 0.20,
        "50 cent": 0.50,
        "1 dollar": 1.00,
        "2 dollar": 2.00,
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        for coin,value in self.COIN_VALUES.items():
            self.money_received += int(input(f"How many {coin} coins?: ")) * value
        # return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            if change > 0:
                print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
