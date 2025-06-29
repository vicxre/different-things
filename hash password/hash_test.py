import hashlib



def my_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

#valid password = vicare13
hash_password = 'f59406461b874c6fc4b3fe15b7b707fb3b242a8efbf9d414312a58692ae34f2f'

while True:
    input_password = input('input password here: ')
    hash_input_password = my_hash(input_password)

    if hash_password == hash_input_password:
        print('password valid!')
        break
    else:
        print('non valid password!!!')


#сделать чтобы хеш проходил автоматический