import time


def parse_line(formulation: str):
    parsed = formulation.split('=')
    return (parsed[0], parsed[1]) if len(parsed) == 2 else None


def worker(x, y):
    print('About to work')
    time.sleep(1)
    print('Done')
    return x + y
