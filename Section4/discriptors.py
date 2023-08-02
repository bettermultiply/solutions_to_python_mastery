class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance.__dict__[self.name] is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print('%s:__delete__' % self.name)
        