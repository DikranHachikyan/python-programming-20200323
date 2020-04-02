value = 100
# 1. декларация
def show(title,*args,**kwargs):
    print(f'positional param:{title}')

    print(f'list of args:' + ','.join(map(str,args)))

    print(f'Keyword arguments:{kwargs}')
    if 'path' in kwargs:
        print(f'path:{kwargs["path"]}')

    if 'log' in kwargs:
        print(f'log file:{kwargs["log"]}')


if __name__ == '__main__':
    # 2. извикване
    #1.
    show('Text Editor')

    #2.
    show('Text Editor',11,12,13)
    
    #3.
    show('Text Editor',14,15,16, path='/usr/local',log='/var/log/editor.log')

    #4.

    appConfig = {
        'user'     :'anna'
        , 'ip'     :'222.333.244.253'
        , 'path'   :'/usr/local'
        , 'log'    : '/var/log/editor.log'
        , 'max_mem':4096
    }

    show('Advanced Editor',234,**appConfig)