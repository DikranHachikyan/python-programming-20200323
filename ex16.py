# декларация
def main():
    users = ['anna','markus','john','maria', 'jane']
    mails = ['anna@no.com','markus@no.com','john@no.com','maria@no.com']


    for data in zip(users,mails):
        name, mail = data
        print(f'{name} => {mail}')
        # print(f'data = {data}')

# извикване
main()