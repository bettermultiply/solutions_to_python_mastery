def descriptor(name, expected_type):
    private_name = '_' + name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected Type: {expected_type}')
        if isinstance(val, int | float) and val < 0:
            raise ValueError(f'Expected non-negative value but find {val}')
        setattr(self, private_name, val)

    return value


def string(name):
    return descriptor(name, str)


def integer(name):
    return descriptor(name, int)


def float_value(name):
    return descriptor(name, float)


class Stock:
    """
    Store
    Stock as

    class
    """
    name = string('name')
    shares = integer('shares')
    price = float_value('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        return cls(row[0], row[1], row[2])

    def __repr__(self):
        return f'Stock(\'{self.name}\', {self.shares}, {self.price})'

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, sold):
        self.shares -= sold

    def __eq__(self, other):
        if isinstance(other, Stock) \
            and (self.name, self.shares, self.price) \
                == (other.name, other.shares, other.price):
            return True
        return False

    def __setattr__(self, key, value):
        if key in self.__dict__:
            super().__setattr__(key, value)
