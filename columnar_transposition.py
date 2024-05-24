class ColumnarCipher:
    def __init__(self):
        self.cipher=''
    def encrypt(self,key,text):
        if key<2 or key>len(text)/2:
            return print('Your Key Is Not Strong Enough')
        columns=['']*key
        for i in range(key):
            currColumn=i
            while currColumn<len(text):
                columns[i]+=text[currColumn]
                currColumn+=key
        return ''.join(columns)
    


    
        