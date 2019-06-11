class Base:
    def foo(self):
        return 'bar'

old_bc = __build_class__
# the base is optional argument because not everything has to have a baseclass
def my_bc(fun, name, base=None, **kw):
    if base is Base:
        print('check if bar method is defined')
        return old_bc(fun, name, **kw)
    if base is not None:
        return old_bc(fun, name, base, **kw)


import builtins
builtins.__build_class__ = my_bc
