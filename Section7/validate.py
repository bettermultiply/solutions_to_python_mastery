import inspect
from functools import wraps


def validated(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        annotations = dict(func.__annotations__)
        ret_check = annotations.pop('return', None)
        signature = inspect.signature(func)
        bind = signature.bind(*args, **kwargs)
        for name, val in annotations.items():
            val.check(bind.arguments[name])
            print(name, ':', val)
        return func(*args, **kwargs)

    return wrapper


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


def enforce(**annotations):
    retcheck = annotations.pop('return_', None)

    def decorate(func):
        sig = signature(func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound = sig.bind(*args, **kwargs)
            errors = []

            # Enforce argument checks
            for name, validator in annotations.items():
                try:
                    validator.check(bound.arguments[name])
                except Exception as e:
                    errors.append(f'    {name}: {e}')

            if errors:
                raise TypeError('Bad Arguments\n' + '\n'.join(errors))

            result = func(*args, **kwargs)

            if retcheck:
                try:
                    retcheck.check(result)
                except Exception as e:
                    raise TypeError(f'Bad return: {e}') from None
            return result
        return wrapper
    return decorate
