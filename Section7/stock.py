from structure import Structure  # , validate_attributes
# from validate import String, PositiveInteger, PositiveFloat


# @validate_attributes
class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, sold: PositiveInteger):
        self.shares -= sold
