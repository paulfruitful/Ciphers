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
    def decrypt(self,key,text):
        columns=['']*key
        for i in range(key):
            currColumn=i
            while currColumn<len(text):
                columns[i]+=text[currColumn]
                currColumn+=key
        return print(''.join(columns))
    
    
    
test=ColumnarCipher()
x=test.encrypt(8,'I got charito my side dish and she couldn\'t ask for more lol ')
test.decrypt(8,x)

    
        