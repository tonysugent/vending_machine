class Product:

    def __init__(self,name,qty,price):
        self.name = name
        self.price = price
        self.qty = qty

    def getQty(self):
        return self.qty

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def setQty(self, newQty):
        self.qty = newQty

    def setName(self,newName):
        self.name = newName

    def setPrice(self,newPrice):
        self.price = newPrice

    def sale(self):
        self.qty -= 1
