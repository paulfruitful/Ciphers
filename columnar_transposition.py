import math
class ColumnarCipher:
  def __init__(self):
        self.cipher=''
  def encrypt(self,key, text):
     if key < 2 or key >= len(text):
        return 'Your Key Is Not Strong Enough'
    
     columns = [''] * key
    
     for i in range(key):
        currColumn = i
        while currColumn < len(text):
            columns[i] += text[currColumn]
            currColumn += key
    
     return ''.join(columns)

  def decrypt(self,key, ciphertext):
    
    
    num_full_rows = len(ciphertext) // key
    num_extra_chars = len(ciphertext) % key
    
    
    columns = [''] * key
    
    index = 0
    
    for i in range(key):
        num_chars_in_column = num_full_rows + (1 if i < num_extra_chars else 0)
        columns[i] = ciphertext[index:index + num_chars_in_column]
        index += num_chars_in_column
    plaintext = []
    for i in range(num_full_rows + 1):
        for col in columns:
            if i < len(col):
                plaintext.append(col[i])
    
    return ''.join(plaintext)



   
    
test=ColumnarCipher()
x=test.encrypt(3,'catholic my man eats hat bick please helperand make sheep so kay')
#test.decrypt(3,x)
plaintext = test.decrypt(3, x)
print(plaintext)

    
        