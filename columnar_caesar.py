from caesar import CaesarCipher
from columnar import ColumnarCipher


class ColsarCipher:
    def encrypt(self, text, key):
        caesar = CaesarCipher()
        columnar = ColumnarCipher()
        
        caesar_cipher = caesar.encrypt(text, key)
        
        columnar_key = int((key * key) % (len(caesar_cipher) / 2))
        
        cipher = columnar.encrypt(columnar_key, caesar_cipher)
        return cipher

    def decrypt(self, cipher, key):
        caesar = CaesarCipher()
        columnar = ColumnarCipher()
        columnar_key = int((key * key) % (len(cipher) / 2))
        columnar_cipher = columnar.decrypt(columnar_key, cipher)
        text = caesar.decrypt(columnar_cipher, key)
        return text




