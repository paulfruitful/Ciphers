
class CaesarCipher:
    def __init__(self) :
        
        self.symbols='abcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()_-+={}[]|\:;\"\',<>./?Δƒ€ŠŒ©®§'
        self.char_dict=  {char: index for index, char in enumerate(self.symbols)}
        
        self.key=None
        self.text=''
        self.cipher=''
    def encrypt(self,text,key):
        if key>len(self.symbols):
            return print('Key can\'t be greater than',len(self.symbols))
        self.key=key
        text=text.lower()
        for i in text:
            curr=self.char_dict[i]
            
            curr=(self.key+curr)%len(self.symbols) 
           
            self.cipher+=self.symbols[curr]
        return self.cipher

    def decrypt(self,text,key):
        if key>len(self.symbols):
            return print('Key can\'t be greater than',len(self.symbols)) 
               
        self.key=key
        for i in text:
            curr=self.char_dict[i]
           
            curr=(curr-self.key)%len(self.symbols)
           
            self.text+=self.symbols[curr]
        
        return self.text
    







        
cat=CaesarCipher()
h=cat.encrypt('Hllo',2)
cat.decrypt(h,2)
