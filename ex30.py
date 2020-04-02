value = 100
# 1. декларация
def show(title,*args,**kwargs):
    print(f'positional param:{title}')

    print(f'list of args:' + ','.join(map(str,args)))

    print(f'Keyword arguments:{kwargs}')
    kw_params = {
        'path' : kwargs.get('path','/tmp')
        , 'log': kwargs.get('log','/var/log/messages')
    }

    print(f'{kw_params}')


if __name__ == '__main__':
    # 2. извикване
    #1.
    show('Text Editor')
    show('Text Editor',11,12,13)
    show('Text Editor',14,15,16, path='/usr/local')
