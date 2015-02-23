import sys
from webant import errors
from webant.utils import snake_case, camel_case


class MetaCapability(type):
    def __init__(cls, name, *args, **kw):
        cls.name = snake_case(name)
        super(MetaCapability, cls).__init__(name, *args, **kw)


class Capability(object):
    __metaclass__ = MetaCapability

    def __new__(self, name=None):
        if name is not None:
            try:
                cap = getattr(sys.modules[__name__], camel_case)
            except:
                raise errors.InvalidCapability(name)

            return cap

    def __eq__(self, other):
        return (self.name == other or
                self.name == getattr(other, 'name', None))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.name)


class AddUser(Capability):
    pass


class DeleteUser(Capability):
    pass


class EditUser(Capability):
    pass


class AddBook(Capability):
    pass


class EditBook(Capability):
    pass


class RemoveBook(Capability):
    pass
