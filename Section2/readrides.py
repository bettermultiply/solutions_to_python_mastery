import csv
import dataclasses
import tracemalloc
from collections import namedtuple


class RowClass:
    def __init__(self, route, date, day_type, rides):
        self.route = route
        self.date = date
        self.day_type = day_type
        self.rides = rides


class RowSlots:
    __slots__ = ['route', 'date', 'day_type', 'rides']

    def __init__(self, route, date, day_type, rides):
        self.route = route
        self.date = date
        self.day_type = day_type
        self.rides = rides


named_rows = namedtuple('named_rows', ['route', 'date', 'day_type', 'rides'])


def read_rides_as_tuples(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            day_type = row[2]
            rides = int(row[3])
            record = (route, date, day_type, rides)
            records.append(record)
    return records


def read_rides_as_dictionary(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            day_type = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'day_type': day_type,
                'rides': rides,
            }
            records.append(record)
    return records


def read_rides_as_class(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            record = RowClass(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records


def read_rides_as_slots(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            record = RowSlots(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records


def read_rides_as_named_rows(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            record = named_rows(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records


if __name__ == '__main__':
    tracemalloc.start()
    rowS = read_rides_as_slots('../Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())

# >>> routes = {s.route for s in rowS}

# >>> people = Counter()
# >>> for record in rowS:
# ...     people[record.route, record.date] += record.rides

# >>> people_rides = Counter()
# >>> for record in rowS:
# ...     people_rides[record.route] += record.rides

# >>> increase = Counter()
# >>> for record in rowS:
# ...     dates = record.date.split('/')
# ...     if int(dates[2]) == 2001:
# ...             increase[record.route] -= record.rides
# ...     elif int(dates[2]) == 2011:
# ...             increase[record.route] += record.rides
# >>> increase.most_common(5)
