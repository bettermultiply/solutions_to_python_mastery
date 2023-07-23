import csv
from collections.abc import Sequence
from sys import intern


class DataCollection(Sequence):
    def __init__(self, names, types):
        self.records = {name: [] for name in names}
        self.names = names
        self.types = types

    def __len__(self):
        return len(self.records[self.names[0]])

    def __getitem__(self, index):
        if isinstance(index, slice):
            record = DataCollection(self.names, self.types)
            for i in range(*index.indices(len(self))):
                record.append({name: self.records[name][i] for name in self.names})
                return record

        return {name: self.records[name][index] for name in self.names}

    def append(self, item):
        for typ, name, value in zip(self.types, item.keys(), item.values()):
            if typ is str:
                self.records[name].append(intern(typ(value)))
            else:
                self.records[name].append(typ(value))


def read_csv_as_columns(filename, types):
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        records = DataCollection(headers, types)
        for row in rows:
            item = {name: value for name, value in zip(headers, row)}
            records.append(item)

    return records

