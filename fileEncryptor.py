from caesar import CaesarCipher


file=input('Path to the file>>>')
encMode=input('What kind of encryption are you using? ')

with open(file,'r') as f:
    content=f.read()
    if encMode.lower().startswith('cae'):
        caesar=CaesarCipher()
        cipher=cae

