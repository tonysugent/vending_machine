class Cashier:
    def __init__(self,cashin,price):
        self.cashin = cashin
        self.price = price

    def makechange(self):
        change = (float(self.cashin) - float(self.price))
        return round(change, 2)