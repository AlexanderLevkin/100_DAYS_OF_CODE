def add(*args):
    print(args[0])
    t = 0
    for n in args:
        t += n
    return t


print(add(3, 5, 6))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)
