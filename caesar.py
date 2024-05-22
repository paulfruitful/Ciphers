
class CaesarCipher:
    def __init__(self,key,text) :
        
        self.symbols='abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_-+={}[]|\:;\"\',<>./?Δƒ€ŠŒ©®§'
        if key<len(self.symbols):
            return print('Key can\'t be greater than 26 ')
        self.key=key
        self.text=text
        self.cipher=''
    def encrypt(self):
        for i in self.text:
            curr=self.symbols.find(i)
            curr=(self.key+curr)-len(self.symbols)
            self.cipher+=self.symbols[curr]
        return print(self.cipher)

    def decrypt(self):
        for i in self.cipher:
            curr=self.symbols.find(i)
            curr=(curr-self.key)-len(self.symbols)
            self.cipher+=self.symbols[curr]
        return print(self.cipher)
    
    def change_text(self,text):
        self.text=text


caat=CaesarCipher(3,'Cat')
caat.encrypt()
caat.decrypt()





        

