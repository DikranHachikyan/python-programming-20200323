# декларация
def main():
    user = {
        'name':'anna'
        , 'mail':'anna@no.com'
        , 'age':30
        , 'phone':'111-22-33'

    }


    for data in user:
        print(f'data = {data} value = {user[data]}')

# извикване
main()