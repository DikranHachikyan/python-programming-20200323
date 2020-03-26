def new_file():
    print('create new file')

def open_file():
    print('open file')

def save_file():
    print('save file')

def quit_app():
    print('quit application')
    quit()

# декларация
def main():
    actions = {
        'n':new_file,
        'o':open_file,
        's':save_file,
        'q':quit_app
    }

    ch = input('Command (n-new,o-open,s-save,q-quit):')

    if ch in actions:
        actions[ch]()
        # new_file() # ако стойността е n
    else:
        print(f'Unknown command ({ch})')

# извикване
main()