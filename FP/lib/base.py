def __call(arg, fn):
  if callable(fn):
    return fn(arg)
  return arg
