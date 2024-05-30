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
   



    def decrypt(self,cipher,key):
        text=''
        for char in cipher:
            if char in self.char_dict:
                curr = self.char_dict[char]
               
                curr = curr//key
                print(curr)
                text+=self.symbols[curr]
            else:
                text+=char
        return text

test=MultiplicationCipher()
a=test.encrypt('My Obi man na  man',1456)
print(test.decrypt(a,1456)) 