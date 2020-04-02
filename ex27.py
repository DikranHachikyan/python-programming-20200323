value = 100
# 1. декларация
def addNumbers(a, b, c = None):
    
    if c is not None:
        res1 = a + b + c
    else:
        res2 = a + b
        
    return res1 if 'res1' in locals() else res2

if __name__ == '__main__':
    # 2. извикване

    x, y = 7, 8
    r = addNumbers(x,y)

    print(f'{x} + {y} = {r}')

    z = 10

    r = addNumbers(x, y, z)
    print(f'{x} + {y} + {z} = {r}')

    # print(globals())


    