import csv


def read_csv_as_instances(filename, instance):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = instance(row[0], int(row[1]), float(row[2]))
            records.append(record)
    return records
