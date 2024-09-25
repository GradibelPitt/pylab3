class Caesar:
    def __init__(self):
        self.__key = 0


    def get_key(self):
        return self.__key


    def set_key(self, key):
        self.__key = key


    def encrypt(self, plaintext):
        ciphertext = ''
        for char in plaintext:
            if char.isalpha():
                shift = (ord(char.lower()) - ord('a') + self.__key) % 26 + ord('a')
                ciphertext += chr(shift)
            elif char.isspace():
                ciphertext += char
            else:
                shift = (ord(char) + self.__key) % 128
                ciphertext += chr(shift)
        return ciphertext


    def decrypt(self, ciphertext):
        plaintext = ''
        for char in ciphertext:
            if char.isalpha():
                shift = (ord(char.lower()) - ord('a') - self.__key) % 26 + ord('a')
                plaintext += chr(shift)
            elif char.isspace():
                plaintext += char
            else:
                shift = (ord(char) - self.__key) % 128
                plaintext += chr(shift)
        return plaintext

cipher = Caesar()

cipher.set_key(3)
print(cipher.encrypt("hello WORLD!"))
print(cipher.decrypt("khoor zruog$"))

cipher.set_key(6)
print(cipher.encrypt("zzz"))
print(cipher.decrypt("fff"))

cipher.set_key(-6)
print(cipher.encrypt("FFF"))

