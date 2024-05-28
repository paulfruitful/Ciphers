class CaesarCipher:
    def __init__(self):
        self.symbols = 'abcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()_-+={}[]|\\:;\"\'<>,.?/Δƒ€ŠŒ©®§'
        self.char_dict = {char: index for index, char in enumerate(self.symbols)}
        self.key = None
        self.cipher = ''
        self.text = ''

    def encrypt(self, text, key):
        
        self.key = key
        self.cipher = ''  # Reset cipher text
        for char in text:
            if char in self.char_dict:
                curr = self.char_dict[char]
                curr = (self.key + curr) % len(self.symbols)
                self.cipher += self.symbols[curr]
            else:
                self.cipher += char  # Keep unknown characters unchanged
        return self.cipher

    def decrypt(self, text, key):
        self.key = key
        self.text = ''  # Reset decrypted text
        for char in text:
            if char in self.char_dict:
                curr = self.char_dict[char]
                curr = (curr - self.key) % len(self.symbols)
                self.text += self.symbols[curr]
            else:
                self.text += char  # Keep unknown characters unchanged
        return self.text


