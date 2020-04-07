
# 1.
# import time

# 2.
# from module_name import func_name, class_name, ...
from time import time


# 3. 
# from module_name import func_name as alias_name, class_name as alias_name2
# from time import time as tm

# def time():
#     pass

if __name__ == '__main__':
    N = 5000
    values = []

    # a
    t = time()
    for v in range(1,N):
        for s in range(1,N):
            values.append( divmod(v,s))
    print(f'for loop:{time()-t:.4f}')

    # b
    t = time()
    values2 = [ divmod(v,s) for v in range(1,N) for s in range(1,N)]
    print(f'for expr:{time()-t:.4f}')

    # c
    t = time()
    values3 = list( (divmod(v,s) for v in range(1,N) for s in range(1,N)) )
    print(f'gen expr:{time()-t:.4f}')