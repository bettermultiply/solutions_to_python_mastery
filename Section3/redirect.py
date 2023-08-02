import sys


class RedirectStdout:
    def __init__(self, out_file):
        self.out_file = out_file

    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self.out_file
        return self.out_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.stdout
