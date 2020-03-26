# декларация
def main():
    x = int(input('x='))

    if x > 0:
        print(f'x is positive ({x})')
        if x >= 5 and x <= 10:
            print(f'x is between 5 and 10 ({x})')
    else:
        print(f'x is negative or 0 ({x})')


# извикване
main()