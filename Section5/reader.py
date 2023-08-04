import csv
import stock
import logging


log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def read_csv_as_dicts(filename: str, types: list, headers=None) -> list:
    """
    Read CSV data into a list of dictionaries with optional type conversion
    """
    with open(filename) as f:
        records = csv_as_dicts(f, types, headers=headers)
    return records


def read_csv_as_instances(filename: str, cls, headers: list[str] = None) -> list:
    """
    Read CSV data into a list of instances
    """
    with open(filename) as f:
        records = csv_as_dicts(f, cls, headers=headers)
    return records


def csv_as_instances(file, cls, headers=None) -> list:
    """
    accept file directly and read CSV data into a list of instances
    """
    records = []
    rows = csv.reader(file)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records


def csv_as_dicts(file, types, headers=None) -> list:
    """
    accept file directly and read CSV data into a list of instances
    """
    records = []
    rows = csv.reader(file)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = {
            name: func(val) for name, func, val in zip(headers, types, row)
        }
        records.append(record)
    return records


def convert_csv(file, func, headers=None) -> list:
    rows = csv.reader(file)
    if headers is None:
        headers = next(rows)
    return list(map(func, [headers], rows))


def convert_csv_exception(filename, types, headers=None):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        if headers is None:
            headers = next(rows)
        for row in rows:
            try:
                record = {
                    name: func(val) for name, func, val in zip(headers, types, row)
                }
                records.append(record)
            except ValueError as e:
                log.warning('Row %s: Bad row: %s', rows.line_num - 1, row)
                log.debug('Row %s: Reason: %s', rows.line_num - 1, e)

    return records


def make_dict(headers, row):
    return dict(zip(headers, row))


def make_stock(headers, row):
    return stock.Stock(*row)


def make_instances(headers, row, cls=None):
    if cls is None:
        raise TypeError('No cls offered')
    return cls(*row)
# in Exercise 5.1 there should be file = gzip.open('../Data/portfolio.csv.gz', 'rt') to open the file in text mode


if __name__ == '__main__':
    line = open('../Data/portfolio.csv')
    convert_csv(line, make_dict)
