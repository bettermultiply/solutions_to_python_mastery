class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'MutInt({self.value!r})'

    def __eq__(self, other):
        if isinstance(other, MutInt):
            return self.value == other.value
        else:
            return NotImplemented
