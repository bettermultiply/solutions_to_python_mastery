class Validator:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, owner, name):
        self.name = name
    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)


class Typed(Validator):
    expected_type = object

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)


class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value <= 0:
            raise ValueError('Expected value > 0')
        return super().check(value)


class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty value')
        return super().check(value)


class Integer(Typed):
    expected_type = int


class Float(Typed):
    expected_type = float


class String(Typed):
    expected_type = str


class PositiveInteger(Positive, Integer):
    pass


class PositiveFloat(Positive, Float):
    pass


class NonEmptyString(NonEmpty, String):
    pass
