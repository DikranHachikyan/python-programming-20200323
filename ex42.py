from time import time, sleep
from functools import  wraps



def measure(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        '''function wrapper'''
        t = time()
        func(*args,**kwargs)
        print(f'{func.__name__}:{time()-t:.4f}')
        print(f'doc string:{func.__doc__}')
    return wrapper

@measure
def foo(sleep_time=0.3):
    '''Function foo sleeps sleep_time seconds'''
    sleep(sleep_time)


if __name__ == '__main__':
    
    foo(0.5)
    foo()

    print(f'{foo.__name__}')
    print(f'doc {foo.__doc__}')
    
