class MultiplicationCipher:
    def __init__(self):
        self.symbols = 'abcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()_-+={}[]|\\:;\"\'<>,.?/Δƒ€ŠŒ©®§'
        self.char_dict = {char: index for index, char in enumerate(self.symbols)}
    def gcd(self,num1,num2):
        if num1==0:
            return num2
        num1,num2 = num2%num1, num1
        return self.gcd(num1,num2)
    def encrypt(self,text,key):
        if self.gcd(key,len(self.symbols))!=1:
            return f'Key must be a prime or co-prime of {len(self.symbols)}'
        cipher=''
        for char in text:
            if char in self.char_dict:
                curr = self.char_dict[char]
                curr = (key * curr) % len(self.symbols)
                cipher+=self.symbols[curr]
            else:
                cipher+=char
        return cipher
    def modularInverse(self,key,symbol):
        if self.gcd(key,symbol)!=1:
            return 'No Modular Inverse '
        u1, u2, u3 = 1, 0, key
        v1, v2, v3 = 0, 1, symbol
        while v3 != 0:
          q = u3 // v3 
          v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
        return u1 % symbol
   



    def decrypt(self,cipher,key):
        text=''
        for char in cipher:
            if char in self.char_dict:
                curr = self.char_dict[char]
               
                curr =(curr*self.modularInverse(key,len(self.symbols)))%len(self.symbols)
             
                text+=self.symbols[curr]
            else:
                text+=char
        return text

class AffineCipher:
    def __init__(self):
        self.symbols = 'abcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()_-+={}[]|\\:;\"\'<>,.?/Δƒ€ŠŒ©®§'
        self.char_dict = {char: index for index, char in enumerate(self.symbols)}
    def gcd(self,num1,num2):
        if num1==0:
            return num2
        num1,num2 = num2%num1, num1
        return self.gcd(num1,num2)
    def modularInverse(self,key,symbol):
        if self.gcd(key,symbol)!=1:
            return 'No Modular Inverse '
        u1, u2, u3 = 1, 0, key
        v1, v2, v3 = 0, 1, symbol
        while v3 != 0:
          q = u3 // v3 
          v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
        return u1 % symbol
    def encrypt(self,text,key,key2):
        if self.gcd(key,len(self.symbols))!=1:
            return f'Key must be a prime or co-prime of {len(self.symbols)}'
        cipher=''
        for char in text:
            if char in self.char_dict:
                curr = self.char_dict[char]
                curr = ((key * curr)+key2) % len(self.symbols)
                cipher+=self.symbols[curr]
            else:
                cipher+=char
        return cipher
    def decrypt(self,cipher,key,key2):
        text=''
        for char in cipher:
            if char in self.char_dict:
                curr = self.char_dict[char]
               
                curr =((curr-key2)*self.modularInverse(key,len(self.symbols)))%len(self.symbols)
             
                text+=self.symbols[curr]
            else:
                text+=char
        return text


test=AffineCipher()
a=test.encrypt('My Obi man na  man',1456,67)
print(test.decrypt(a,1456,67)) 