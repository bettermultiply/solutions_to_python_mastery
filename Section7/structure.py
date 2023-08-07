import sys
import inspect
from validate import Validator, validated


class Structure:
    _fields = ()
    _types = ()
    # def __init__(self, *value):
    #     if len(value) != len(self._fields):
    #         raise TypeError('Expected %d' % len(self._fields))
    #     for key, value in zip(self._fields, value):
    #         self.__setattr__(key, value)

    # @staticmethod
    # def _init():
    #     locs = sys._getframe(1).f_locals
    #     self = locs.pop('self')
    #     for name, val in locs.items():
    #         setattr(self, name, val)

    @classmethod
    def from_row(cls, row):
        print(cls._types)
        rowdata = [func(val) for func, val in zip(cls._types, row)]
        return cls(*rowdata)

    @classmethod
    def set_fields(cls):
        sig = inspect.signature(cls)
        cls._fields = list(sig.parameters)

    @classmethod
    def create_init(cls):
        args = ','.join(cls._fields)
        code = f'def __init__(self, {args}):\n'
        for name in cls._fields:
            code += f'\tself.{name} = {name}\n'

        locs = {}
        exec(code, locs)
        cls.__init__ = locs['__init__']

    @classmethod
    def __init_subclass__(cls, **kwargs):
        validate_attributes(cls)

    def __repr__(self):
        report = self.__class__.__name__
        content = ', '.join(repr(self.__dict__[key]) for key in self._fields)
        # for key in self._fields:
        #     value = self.__dict__[key]
        #     if isinstance(value, str):
        #         report += f"'{value}'"
        #     else:
        #         report += str(value)
        #     report += ',' if key != self._fields[-1] else ')'
        report += f'({content})'
        return report

    def __setattr__(self, key, value):
        if key not in self._fields and not key.startswith('_'):
            raise AttributeError('No attribute %s' % key)
        super().__setattr__(key, value)


def validate_attributes(cls):
    validators = []
    types = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)
            types.append(val.expected_type)
        elif callable(val) and val.__annotations__ :
            setattr(cls, name, validated(val))
    cls._fields = [val.name for val in validators]
    cls._types = list(types)
    cls.create_init()
    return cls


