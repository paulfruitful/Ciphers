import math
class ColumnarCipher:
    def __init__(self):
        self.cipher=''
    def encrypt(self,key,text):
        if key<2 or key>=len(text):
            return print('Your Key Is Not Strong Enough')
        columns=['']*key
        for i in range(key):
            currColumn=i
            while currColumn<len(text):
                columns[i]+=text[currColumn]
                currColumn+=key
        print(''.join(columns))
        return ''.join(columns)
    def decrypt(self, key, cipher):
        if key < 2 or key >= len(cipher):
            return 'Your Key Is Not Strong Enough'

        numOfrows = int(round(float(len(cipher)) / float(key), 0))  # Convert the rounded result to an integer
        numOfcols = key
        plaintext = [''] * numOfrows
        col=0
        row=0
        for i in range(len(cipher)):
         currCol=col
         while currCol<len(cipher) :
           plaintext[row] += cipher[currCol]  # Append the character to the current row
           print(currCol,cipher[currCol])
           currCol+=numOfrows
         
         col += 1
      
        print(len(cipher))
        print(len(''.join(plaintext)))
        return print(''.join(plaintext))
   
    
test=ColumnarCipher()
x=test.encrypt(3,'Igotcharito mysidedishandshe couldnt a skformorelol ')
test.decrypt(3,x)

    
        