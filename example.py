def f(x):
  print x*x

def g(x):
  return x % 2 == 0

def apply_filter(iterable, f, g):
  def gen_filter(iterable):
    for elt in iterable:
      if g(elt):
        yield elt

  for elt in gen_filter(iterable):
    f(elt)

apply_filter(set(range(10)), f, g)

