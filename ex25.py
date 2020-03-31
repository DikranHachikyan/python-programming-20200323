
# 1. декларация
def addNumbers(a, b, c = 0):
    res = a + b + c
    return res

if __name__ == '__main__':
    # 2. извикване

    x, y = 7, 8
    r = addNumbers(x,y)

    print(f'{x} + {y} = {r}')

    z = 10

    r = addNumbers(x, y, z)
    print(f'{x} + {y} + {z} = {r}')


    