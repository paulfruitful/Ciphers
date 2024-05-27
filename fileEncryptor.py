from caesar import CaesarCipher
from columnar import ColumnarCipher

def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def write_file(file_path, content):
    try:
        with open(file_path, 'w') as f:
            f.write(content)
    except Exception as e:
        print(f"Error writing file: {e}")

def main():
    file_path = input('Path to the file>>> ')
    mode = input('Are you (e)ncrypting or (d)ecrypting? ')
    print(''' Encryption Algorithms Available For Now:
          - Caesar Cipher
          - Columnar Transposition Cipher

 ''')
    enc_mode = input('What kind of encryption are you using? ')
    key = int(input('Enter a key>>> '))
    
    content = read_file(file_path)
    if content is None:
        return

    caesar = CaesarCipher()
    columnar=ColumnarCipher()

    if mode.startswith('e') and enc_mode.lower() == 'caesar':
        cipher = caesar.encrypt(content, key)
        write_file(file_path, cipher)
        print("File encrypted successfully.")
    if mode.startswith('e') and enc_mode.lower() == 'columnar':
        cipher = columnar.encrypt(key,content)
        write_file(file_path, cipher)    
        print("File encrypted successfully.") 
    if mode.startswith('d') and enc_mode.lower() == 'columnar':
        cipher = columnar.decrypt(key,content)
        print("File decrypted successfully.")
        write_file(file_path, cipher)       
    if mode.startswith('d') and enc_mode.lower() == 'caesar':
        text = caesar.decrypt(content, key)
        write_file(file_path, text)
        print("File decrypted successfully.")
    else:
        print("Invalid mode or encryption type selected.")

if __name__ == "__main__":
    main()
