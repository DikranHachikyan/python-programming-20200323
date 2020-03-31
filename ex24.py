# Глобална променлива
value = 100
# 1. декларация
def addNumbers(first_number, second_number):
    # result - локална променлива
    result = first_number + second_number
    # if True :
    #     result =1 блок прилежащ на обл. addNumbers
    return result

if __name__ == '__main__':
    # 2. извикване
    a, b = 5, 6
    suma = addNumbers(a, b)

    print(f'{a}+{b}={suma}')
    print(f'value={value}')