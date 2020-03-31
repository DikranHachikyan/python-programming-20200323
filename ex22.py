# 1. декларация
def addNumbers(first_number, second_number):
    print(f'{first_number}+{second_number}={first_number+second_number}')


if __name__ == '__main__':
    # 2. извикване
    a, b = 5, 6
    addNumbers(a, b)