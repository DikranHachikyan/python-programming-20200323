value = 100
# 1. декларация
def addNumbers(a, b, *args):
    # print(type(args))
    # print(args)

    res = a + b
    for v in args:
        res += v
    return res
    

if __name__ == '__main__':
    # 2. извикване

    x, y = 7, 8
    r = addNumbers(x,y)

    print(f'{x} + {y} = {r}')
    
    r = addNumbers(x,y,1,2,3,4,5,6)

    print(f'{x} + {y} + .... = {r}')

    lst = list(range(6))

    r = addNumbers(x,y, *lst)
    print(f'{x} + {y} + ' + ' + '.join( str(v) for v in lst)  + f' = {r}')