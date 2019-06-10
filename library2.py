class Base:
    def foo(self):
        return self.bar


#there is a function __build_class in python. It sits on a module builtins
old_bc = __build_class__
def my_bc(fun, name, base=None, **kw):
    if base is Base:
        print('check if bar method defined')
    if base is not None:
        old_bc(fun, name, base, **kw)
    return old_bc(fun, name, **kw)
#we capture the original build class, write our own build clas

import builtins
#we make import from builtins ans swap out our classes
#so we are patching creating classes in python
builtins.__build_class__ = my_bc
