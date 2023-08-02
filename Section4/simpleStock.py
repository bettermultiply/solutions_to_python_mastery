from validate import *


class SimpleStock:
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price
