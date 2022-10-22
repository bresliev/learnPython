def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


def calculate(n, **kwargs):
    print(kwargs)

    n += kwargs["add"]
    print(n)
    n *= kwargs["miulti"]
    print(n)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")



