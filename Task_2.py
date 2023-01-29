# Шифр Цезаря

def encrypt_caesar(msg,shift):
    if msg.isalpha():
        number = ord(msg) + shift % 32
        if number  > 1103:
            number -= 32
        return chr(number)
    return msg
 
shift = int(input('Шаг шифровки: '))
for l in input('Сообщение для шифровки: '):
    print(encrypt_caesar(l, shift), end='')

def decrypt_caesar(msg,shift):
    if msg.isalpha():
        number = ord(msg) - shift % 32
        if number  > 1103:
            number -= 32
        return chr(number)
    return msg
print ()
shift = int(input('Шаг шифровки: '))
for l in input('Сообщение для шифровки: '):
    print(decrypt_caesar(l, shift), end='')