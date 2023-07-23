import csv


def read_csv_as_dicts(filename, types):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        heading = next(rows)
        for row in rows:
            record = {name: func(value) for name, func, value in zip(heading, types, row)}
            records.append(record)
    return records
