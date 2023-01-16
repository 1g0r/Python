import lib.base as l
from functools import reduce

def a(fn):
    print('Enter a', end='')
    if callable(fn):
        fn('a')
    print(' Exit a')

def b(fn):
    print('Enter b', end='')
    if callable(fn):
        fn('b')
    print(' Exit b')

def c(fn):
    print('Enter c', end='')
    if callable(fn):
        fn('c')
    print(' Exit c')
def d(*a):
    print(a)

def tt(fn1):
    def _tt(fn2):
        fn1(fn2)
    return _tt

def wf(fn1):
    funcs = [fn1]
    def _n(fn2):
        if callable(fn2):
            funcs.append(fn2)
            return _n
        for fn in reversed(funcs):

    return _n
t=wf(a)(b)(c)
t(0)ls