import collections
import csv
import dataclasses
import tracemalloc
from collections import namedtuple

file = '../Data/ctabus.csv'


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


class RideData(collections.abc.Sequence):
    def __init__(self):
        self.route = []
        self.date = []
        self.day_type = []
        self.rides = []

    def __len__(self):
        return len(self.route)

    def __getitem__(self, index):
        if isinstance(index, slice):
            new_ride = RideData()
            for i in range(index.start, index.stop):
                new_ride.append(self[i])
            return new_ride

        return {
            'route': self.route[index],
            'date': self.date[index],
            'day_type': self.day_type[index],
            'rides': self.rides[index],
        }

    # def __repr__(self):
    #     pass

    def append(self, item):
        self.route.append(item['route'])
        self.date.append(item['date'])
        self.day_type.append(item['day_type'])
        self.rides.append(item['rides'])



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
    # records = []
    records = RideData()
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


def read_rides_as_columns(filename):
    routes = []
    dates = []
    day_type = []
    num_rides = []
    with open(filename) as f:
        rows = csv.reader(f)
        heading = next(rows)
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            day_type.append(row[2])
            num_rides.append(int(row[3]))
    return dict(routes=routes, dates=dates, day_type=day_type, num_rides=num_rides)



# if __name__ == '__main__':
#     tracemalloc.start()
#     rowS = read_rides_as_slots('../Data/ctabus.csv')
#     print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())

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
