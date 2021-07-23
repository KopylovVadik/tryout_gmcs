def cube(i):
    return i ** 3


result = map(cube, [i for i in range(0, 11)])

print(list(result))
