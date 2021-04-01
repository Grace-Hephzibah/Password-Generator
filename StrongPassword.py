def PWD():
    maximum_length = 12

    upper = [chr(i) for i in range(65,91)]
    lower = [chr(i) for i in range(97,123)]
    number = [chr(i) for i in range(48,57)]
    special_char = ['@','$','!','#','%','^','&','*','(',')']

    combine = upper + lower + number + special_char

    import random

    password_generated = ""

    for i in range(maximum_length):
        password_generated += random.choice(combine)

    return password_generated

    

