value = 100
# 1. декларация
def show(title,*args,k1,k2,**kwargs):
    print(f'positional param:{title}')
    print(f'list of args:' + ','.join(map(str,args)))
    print(f'Keyword arguments:{kwargs}')
    print(f'Keyword only: k1={k1} k2={k2}')

if __name__ == '__main__':
    # 2. извикване
    show('Text Editor',k1='F',k2='R')
    show('Text Editor',*(3,5,7), k1='FX',k2='RX')
    show('Text Editor',13,25,37, k1='FX',k2='RX',ip='127.0.0.1')
    show('Text Editor',k1='FX',k2='RX',*(13,25,37),ip='127.0.0.1')