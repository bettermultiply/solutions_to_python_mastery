import csv


class Stock:
    __slots__ = ("name", "_shares", "_price")

    _types = (str, int, float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __str__(self):
        return '%s-%d-%f' % self.name, self.shares, self.price

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"

    def __eq__(self, other):
        return isinstance(other, Stock)\
                and (self.name, self.shares, self.price) ==\
                    (other.name, other.shares, other.price)

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types.__getitem__(1)):
            raise TypeError('Expected %s' % self._types[1])
        elif value < 0:
            raise ValueError('Expected positive value')
        self._shares = value

    @shares.getter
    def shares(self):
        return self._shares

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, self._types.__getitem__(2)):
            raise TypeError('Expected %s' % self._types[2])
        elif value < 0:
            raise ValueError('Expected positive value')
        self._price = value

    @price.getter
    def price(self):
        return self._price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, sold_shares):
        self.shares -= sold_shares


def read_portfolio(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            name = row[0]
            shares = int(row[1])
            price = float(row[2])
            s = Stock(name, shares, price)
            records.append(s)
    return records


def print_portfolio(portfolio: []):
    print('%10s %10s %10s' % ('name', 'shares', 'price'))
    print(('-'*10 + ' ')*3)
    for p in portfolio:
        print("%10s %10d %10.3f" % (p.name, p.shares, p.price))
        