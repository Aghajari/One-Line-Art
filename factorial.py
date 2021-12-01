inp = int(input())

print(__import__('functools').reduce(lambda x, y: x * y, range(1, inp + 1)))

print((lambda f: lambda x: f(f, x))(lambda f, x: x if x <= 1 else x * f(f, x - 1))(inp))

print([a := i * globals().get('a', 1) for i in range(1, inp + 1)][-1])
