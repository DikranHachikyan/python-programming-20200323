def show():
    print('function show')

# декларация
def main():
    
    i = 1
    n_sum = 0

    while i <= 3:
        n_sum += i
        i += 1

    show()
    print(f'1 + 2 + 3 = {n_sum}')

# извикване
main()