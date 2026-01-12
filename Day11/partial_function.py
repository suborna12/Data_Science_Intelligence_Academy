from functools import partial
def power(base, exp):
    return base ** exp

sqr = partial(power, exp=2)
print(sqr(4))