from time import time, sleep

def foo(sleep_time=0.3):
    '''Function foo sleeps sleep_time seconds'''
    sleep(sleep_time)


def measure(func):
    def wrapper(*args,**kwargs):
        '''function wrapper'''
        t = time()
        func(*args,**kwargs)
        print(f'{func.__name__}:{time()-t:.4f}')
        print(f'doc string:{func.__doc__}')
    return wrapper

if __name__ == '__main__':
    
    f = measure(foo)

    f(0.5)
    f()
    print(f'f is {f.__name__}')
    print(f'f doc {f.__doc__}')
