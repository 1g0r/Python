from functools import reduce

def __call(arg, fn):
  if callable(fn):
    return fn(arg)
  return arg

def pipe(*funcs):
  if not funcs:
    raise Exception('Supply functions to the pipe function!')
  def __run_pipe(data):
    return reduce(__call, funcs, data)
  return __run_pipe

def compose(*funcs):
  if not funcs:
    raise Exception('Supply functions to the compose function!')
  def __run_compose(data):
    return reduce(__call, reversed(funcs), data)
  return __run_compose

def memoize(fn):
  cache = {}
  def __run_fn(*args):
    if args in cache:
      return cache[args]
    cache[args] = fn(*args)
    return cache[args]
  return __run_fn

if __name__ == '__main__':
  def add2(val):
    return 2 + val
  def mul2(val):
    return 2 * val
  def toList(val):
    return [val]
  
  addMul = pipe(add2, mul2, toList)
  mulAdd = pipe(mul2, add2, toList)
  print('  pipe: AddMul =', addMul(3), 'MulAdd =', mulAdd(3))
  addMul = compose(toList, mul2, add2)
  mulAdd = compose(toList, add2, mul2)
  print('  compose: AddMul =', addMul(3), 'MulAdd =', mulAdd(3))
  
  print('memo:')
  def add(a ,b):
    print(f'{a} + {b} = ', end='')
    return a + b
  mAdd = memoize(add)
  print(mAdd(3, 2))
  print(mAdd(3, 2))
