import unittest
import stock


class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEquals(s.name, 'GOOG')
        self.assertEquals(s.shares, 100)
        self.assertEquals(s.price, 490.1)

    def test_create_with_keyword(self):
        s = stock.Stock(name='GOOG', shares=100, price=490.1)
        self.assertEquals(s.name, 'GOOG')
        self.assertEquals(s.shares, 100)
        self.assertEquals(s.price, 490.1)

    def test_cost(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEquals(s.cost, 100 * 490.1)

    def test_sell(self):
        s = stock.Stock('GOOG', 100, 490.1)
        s.sell(50)
        self.assertEquals(s.shares, 100 - 50)

    def test_from_row(self):
        s = stock.Stock.from_row(['GOOG', 100, 490.1])
        self.assertEquals(s.name, 'GOOG')
        self.assertEquals(s.shares, 100)
        self.assertEquals(s.price, 490.1)

    def test_repr(self):
        s = stock.Stock.from_row(['GOOG', 100, 490.1])
        self.assertEqual(repr(s), "Stock('GOOG', 100, 490.1)")

    def test_eq(self):
        s1 = stock.Stock.from_row(['GOOG', 100, 490.1])
        s2 = stock.Stock.from_row(['GOOG', 100, 490.1])
        self.assertTrue(s1 == s2)

    def test_shares_bad_type(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.shares = '50'

    def test_negative_bad_value(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(ValueError):
            s.shares = -50

    def test_price_bad_type(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.price = '397.2'

    def test_price_bad_value(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(ValueError):
            s.price = -397.2

    def test_bad_attribute(self): # using __slots__ to solve this error
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(AttributeError):
            s.share = 100


if __name__ == '__main__':
    unittest.main()