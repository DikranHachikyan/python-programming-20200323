# декларация
def main():
    users = ['anna','markus','john','maria', 'jane']
    mails = ['anna@no.com','markus@no.com','john@no.com','maria@no.com']
    hash = {}

    for data in zip(users,mails):
        name, mail = data
        hash[name] = mail
    
    print(hash)

# извикване
main()