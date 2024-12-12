def gen1():
    yield 10
    yield 20
    yield 30
    yield 40


gen1()
next(gen1())
x = gen1()
next(x)
next(x)
next(x)
next(x)


def gen2():
    for i in range(10):
        yield i


y = gen2()
next(y)
next(y)
