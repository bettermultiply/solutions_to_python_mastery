import sys
import inspect


class Structure:
    _fields = ()
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

    def __repr__(self):
        report = self.__class__.__name__ + '('
        for key in self._fields:
            value = self.__dict__[key]
            if isinstance(value, str):
                report += f"'{value}'"
            else:
                report += str(value)
            report += ',' if key != self._fields[-1] else ')'
        return report

    def __setattr__(self, key, value):
        if key not in self._fields and not key.startswith('_'):
            raise AttributeError('No attribute %s' % key)
        super().__setattr__(key, value)
