from caesar import CaesarCipher


file=input('Path to the file>>>')
mode=input('Are you (e)ncrypting or (d)ecrypting?')
key=int(input('Enter a key>>> '))
encMode=input('What kind of encryption are you using? ')
content=''
with open(file,'r') as f:
   content=f.read()

if mode.startswith('e'):
 with open(file,'w+') as f:
    if encMode=='caesar':
        caesar=CaesarCipher()
        cipher=caesar.encrypt(content,key)
      
        f.write(cipher)


else:
  with open(file,'w+') as f:
    if encMode=='caesar':
        caesar=CaesarCipher()
        text=caesar.decrypt(content,key)
        print(text)
        f.write(text)

   



