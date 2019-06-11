class Base:
    def foo(self):
        return 'bar'


# we capture the original build class
old_bc = __build_class__

# we write our own build class
def my_bc(*a, **kw):
    print('my buildclass -->', a, kw)
    return old_bc(*a, **kw)


# there is a function __build_class in python. It sits on a module builtins
import builtins
# we make import from builtins ans swap out our classes
# so we are patching creating classes in python
builtins.__build_class__ = my_bc

# and here we can patch into what python actually does when
# it creates classes
