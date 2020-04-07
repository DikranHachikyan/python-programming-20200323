# 1. декларация

def calc_squares(n):
    return [ v ** 2 for v in range(n+1)]

# 1. декларация
def gen_squares(n):
    for v in range(n+1):
        yield v ** 2

if __name__ == '__main__':
    
    values = calc_squares(10)

    print(f'values={values}')
    
    # 2. присвояване на генератора на променлива
    sq = gen_squares(10)

    # print(type(gen_squares))
    # print(type(sq))

    print(f'1=>{next(sq)}')
    print(f'2=>{next(sq)}')
    print(f'3=>{next(sq)}')
    print(f'4=>{next(sq)}')
    print(f'5=>{next(sq)}')

    sq1 = gen_squares(3)
    print(f'1=>{next(sq1)}')
    print(f'2=>{next(sq1)}')
    print(f'3=>{next(sq1)}')
    print(f'4=>{next(sq1)}')
    print(f'5=>{next(sq1)}')
    