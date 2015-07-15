import ctypes
import sys
import atexit

class PyObject(ctypes.Structure):
    _fields_ = [
        ('ob_refcnt', ctypes.c_long),
        ('ob_type', ctypes.c_void_p),
    ]

class SafeZero(int):
    def __new__(self):
        return int.__new__(self, 0)

    def __rdiv__(self, other):
        if other > 0:
            # nobody goes higher than this, right?
            return sys.maxint

        return -sys.maxint - 1

class Replaced(object):
    def __init__(self):
        # Keep references safely inside this object
        self.replaced = []

    def add(self, old, new):
        _old = PyObject.from_address(id(old))
        _new = PyObject.from_address(id(new))

        old_type = _old.ob_type
        old_refcnt = _old.ob_refcnt

        _new.ob_refcnt += old_refcnt
        _old.ob_type = _new.ob_type

        self.replaced.append((_old, _new, old_type, old_refcnt, new))

    def __del__(self):
        for _old, _new, old_type, old_refcnt, new in self.replaced:
            _old.ob_type = old_type
            _new.ob_refcnt -= old_refcnt
            # new is now safe to delete

        del self.replaced[:]

replaced = Replaced()
replaced.add(0, SafeZero())

@atexit.register
def cleanup():
    global replaced
    del replaced

