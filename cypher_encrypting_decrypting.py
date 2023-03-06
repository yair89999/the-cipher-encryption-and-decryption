import random


characters_string = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_+=-[]{}'\|<>,./?`"
# you can add more characters to make it more secure and harder for breach
characters_list = []
for s in characters_string:
    characters_list.append(s)


to_encrypt = input("Enter the string you want to encrypt:")
def encrypt(to_encrypt:str):
    key = random.randint(0,(len(characters_list)-1)*2)**5 # to make it harder to breach
    encrypted = ""
    for s in to_encrypt:
        i = characters_list.index(s)
        i += key
        i = i % (len(characters_list)-1)
        encrypted += characters_list[i]
    return encrypted,key
encrypted,key = encrypt(to_encrypt)
print("not encrypted: " + to_encrypt)
print("encrypted:     " + encrypted)
print("to decrypt use this key:",key)

def decrypt(to_decrypt:str,key:int):
    decrypted = ""
    for s in to_decrypt:
        i = characters_list.index(s)
        i -= key
        i = i % (len(characters_list)-1)
        i = abs(i)
        decrypted += characters_list[i]
    return decrypted

decrypted = decrypt(encrypted,key)
print("encrypted: " + encrypted)
print("decrypt:   " + decrypted)
print("key used:",key)
