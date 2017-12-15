from simplecrypt import encrypt, decrypt
from os.path import exists
from os import unlink


with open('passwords/gmail.txt', 'rb') as input:
    ciphertext2 = input.read()
    plaintext3 = decrypt('P24KYeMzkXNRr3gV', ciphertext2)
    plaintext4 = (plaintext.decode('utf8'))
    print (plaintext4)