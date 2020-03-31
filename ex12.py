# декларация
def main():
    # 2 + 4 + .... + 98 + 100 

    i = 1
    n_sum = 0

    while i <= 100:
        i += 1
        if i > 3: break
        n_sum += i
    else:
        print('else after while')

    print(f'2 + 4 + ... + 98 + 100 = {n_sum}')

# извикване
main()