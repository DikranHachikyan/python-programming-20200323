from functools import  wraps

def upperCase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.__original = func
        args = [ str(v).upper() for v in args]
        return func(*args, **kwargs)
    return wrapper


@upperCase
def concat(*args,**kwargs):
    sep = kwargs.get('sep',';')
    return sep.join(args)

if __name__ == '__main__':
    
    langs = ['python','c','c++','java']

    print(concat('anna','maria','john','markus',sep=' / '))
    print(concat.__original(*langs))
    print(concat(11,23,4,56,7,9, sep=' - '))

    print = upperCase(print)
    print('hello python')
    print = print.__original
    print('hello python')
