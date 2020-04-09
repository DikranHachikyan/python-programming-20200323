
if __name__ == '__main__':
    cube = lambda a: a ** 3
    foo  = lambda a: a ** 3 if a % 2 else a ** 2

    print(f'3 ^ 3 = {cube(3)}')
    print(f'foo = {foo(3)}')
    print(f'foo = {foo(4)}')

    items = [('A', 5, 7), ('Z', 2, 6), ('B', 4,6), ('D', 2,5)]

    # 1.
    # items.sort()
    # print(f'sorted in place:{items}')

    # 2. 
    # items.sort(key=lambda el: el[1])
    # print(f'sorted in place:{items}')

    items.sort( key=lambda el: (el[1],el[0]))
    print(f'sorted in place:{items}')


    values = [1,2,3,4,5]
    for v in map(lambda a: a * 2, values):
        print(v)
