'''
# REVERSED ORDER
tc = lambda f: c(f)
tb = lambda f: b(tc)
ta = lambda f: a(tb)

# DIRECT ORDER
ta = lambda f: a(f)
tb = lambda f: ta(lambda x: b(f))
tc = lambda f: tb(lambda x: c(x))
'''
def flatten(*fns, direct=True):
    if direct:
        return __direct(*fns)
    return __reverse(*fns)
    
def curring(fn):
    result = __wrap_direct(None, fn)
    def _do_loop(f):
        if callable(f):
            nonlocal result
            result = __wrap_direct(result, f)
            return _do_loop
        return result(f)
    return _do_loop
    
def __direct(*fns):
    result = None
    for fn in fns:
        result = __wrap_direct(result, fn)
    return result
    
def __reverse(*funcs):
    result = None
    for fn in reversed(funcs):
        result = __wrap_reverce(fn, result)
    return result
    
def __wrap_direct(prev, cur):
    if not prev:
        return lambda f: cur(f)
    def _p(fn):
        if callable(fn):
            return lambda x: cur(fn)
        return lambda x: cur(x)
    def _t(fn):
        return prev(_p(fn))
    return _t
    
def __wrap_reverce(cur, nxt):
    if not nxt:
        return lambda f: cur(f)
    return lambda f: cur(nxt)
    
if __name__ == '__main__':
    def a(fn):
        print(' <a> ', end='')
        if callable(fn):
            fn('a')
        else:
            print(fn, end='')
        print(' </a> ', end='')
        
    def b(fn):
        print(' <b> ', end='')
        if callable(fn):
            fn('b')
        else:
            print(fn, end='')
        print(' </b> ', end='')
        
    def c(fn):
        print(' <c> ', end='')
        if callable(fn):
            fn('c')
        else:
            print(fn, end='')
        print(' </c> ', end='')
        
    flatten(a,b,c)(0); print('')
    flatten(a,b,c, direct=False)(0); print('')
    curring(a)(b)(c)(0); print('')
