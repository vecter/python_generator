def f(x):
  print x*x

def g(x):
  return x % 2 == 0

def apply_filter(lst, f, g):
  def gen_filter(lst):
    for elt in lst:
      if g(elt):
        yield elt

  for elt in gen_filter(lst):
    f(elt)

apply_filter(range(10), f, g)

