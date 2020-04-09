from functools import  wraps

def upperCase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # args = [ f'{v}'.upper() for v in args]
        args = [ str(v).upper() for v in args]
        return func(*args, **kwargs)
    return wrapper

def brackets(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        args = [ f'[{v}]' for v in args]
        return func(*args,**kwargs)
    return wrapper

@upperCase
@brackets
def concat(*args,**kwargs):
    sep = kwargs.get('sep',';')
    return sep.join(args)

if __name__ == '__main__':
    
    langs = ['python','c','c++','java']

    print(concat('anna','maria','john','markus',sep=' / '))
    print(concat(*langs))
    print(concat(11,23,4,56,7,9, sep=' - '))


    # print = upperCase(print)
    # print('hello python')
    
    printUC = upperCase(print)
    printUC('hello python')
