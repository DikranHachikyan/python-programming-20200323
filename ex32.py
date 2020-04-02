value = 100
# 1. декларация
def show(title,*,k1,k2):
    print(f'positional param:{title}')
    print(f'Keyword only: k1={k1} k2={k2}')

if __name__ == '__main__':
    # 2. извикване
    show('Text Editor',k1='F',k2='R')
    show('Text Editor',k1='FX',k2='RX')
    