message = input('enter the message: ')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
encrypt = ''
decrypt = ''
for i in message:
    position = alphabet.find(i)
    newposition = (position+key)%26
    encrypt += alphabet[newposition]

print("encrypted message = " +encrypt)

for i in encrypt:
    pos = alphabet.find(i)
    newposition = (pos-key) % 26
    decrypt += alphabet[newposition]
print("decripted message = " +decrypt)
