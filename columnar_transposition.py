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

        numOfColumns = len(cipher) // key
        numOfRows = key
        numOfShadedBoxes = (numOfColumns * numOfRows) - len(cipher)

        plaintext = [''] * numOfColumns
        column = 0
        row = 0
        for symbol in cipher:
         plaintext[column] += symbol
         column += 1

         if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

        return print(''.join(plaintext))
    
    
test=ColumnarCipher()
x=test.encrypt(3,'I got charito my side dish and she couldn\'t ask for more lol ')
test.decrypt(3,x)

    
        