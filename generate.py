def password_generator(n,length):
    import random
    import string 

    lower = list(string.ascii_lowercase)
    numbers = list(string.digits)
    special = list(string.punctuation)
    upper = list(string.ascii_uppercase)
    listAll = lower+numbers+special+upper 

    password = []

    combination = ""

    n = int(input("How many passwords do you want to generate: "))
    length = int(input("Enter length of password: "))

    for i in range(n):
        combination = ""
        for j in range(length):
            combination += str(random.choice(listAll))
        password.append(combination)

    print(password)