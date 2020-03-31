# декларация
def main():
    user = {
        'name':'anna'
        , 'mail':'anna@no.com'
        , 'age':30
        , 'phone':'111-22-33'

    }


    for item in user.items():
        key,value = item
        print(f'key = {key} value = {value}')

# извикване
main()