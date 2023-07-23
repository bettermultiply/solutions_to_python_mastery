from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
file = '../Data/portfolio3.dat'


def read_stock_file(filename):
    stockTuple = []
    with open(filename) as f:
        for line in f:
            t = line.split()
            try:
                share = int(t[1])
                price = float(t[2])
            except ValueError as e:
                print(f'Couldn\'t parse \'{line}\' Autofilled by 0.0\nReason:', e, '\n')
                share = 0
                price = 0.0
            stockTuple.append(Stock(t[0], share, price))
    return stockTuple


def calculate(stocks):
    total = 0.0
    for stock in stocks:
        s = stock.shares * stock.price
        total += s
    print('total:', total)


if __name__ == '__main__':
    Stocks = read_stock_file(file)
    calculate(Stocks)
