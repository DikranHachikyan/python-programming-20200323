# декларация
def main():
    lst = [ x ** 2 for x in range(10)]

    print(lst)

    letters = [ f'[{v}]' for v in 'hello python']

    print(letters)

    print('-'.join(letters))

# извикване
main()