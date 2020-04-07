# 1. декларация

def calc_squares(n):
    return [ v ** 2 for v in range(n+1)]

# 1. декларация
def gen_squares(n):
    for v in range(n+1):
        yield v ** 2

def gen_letters(text):
    for t in text:
        yield t

if __name__ == '__main__':
    
    # 1
    for v in gen_squares(5):
        print(f'v={v}')

    # 2
    ls = list(gen_squares(5))
    print(f'ls={ls}')


    txt = list(gen_letters('Hello Python'))
    print(f'txt={txt}')