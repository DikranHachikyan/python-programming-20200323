# 1. декларация
def addNumbers(first_number, second_number):
    result = first_number + second_number
    return result

if __name__ == '__main__':
    # 2. извикване
    a, b = 5, 6
    suma = addNumbers(a, b)

    print(f'{a}+{b}={suma}')