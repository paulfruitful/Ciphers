from caesar import CaesarCipher
from columnar import ColumnarCipher
from columnar_caesar import ColsarCipher

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def write_file(file_path, content):
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        print(f"Error writing file: {e}")

def main():
    file_path = input('Path to the file>>> ')
    mode = input('Are you (e)ncrypting or (d)ecrypting? ').strip().lower()
    print(''' Encryption Algorithms Available For Now:
          - Caesar Cipher
          - Columnar Transposition Cipher
          - Columnar + Caesar Cipher (Colsar)

    ''')
    enc_mode = input('What kind of encryption are you using? ').strip().lower()
    key = int(input('Enter a key>>> '))
    
    content = read_file(file_path)
    if content is None:
        return

    caesar = CaesarCipher()
    columnar = ColumnarCipher()
    colsar = ColsarCipher()

    if mode == 'e':
        if enc_mode == 'caesar':
            cipher = caesar.encrypt(content, key)
            write_file(file_path, cipher)
            print("File encrypted successfully.")
        elif enc_mode == 'colsar':
            cipher = colsar.encrypt(content, key)
            write_file(file_path, cipher)
            print("File encrypted successfully.")
        elif enc_mode == 'columnar':
            cipher = columnar.encrypt(key, content)
            write_file(file_path, cipher)
            print("File encrypted successfully.")
        else:
            print("Invalid encryption type selected.")
    elif mode == 'd':
        if enc_mode == 'caesar':
            text = caesar.decrypt(content, key)
            write_file(file_path, text)
            print("File decrypted successfully.")
        elif enc_mode == 'colsar':
            text = colsar.decrypt(content, key)
            write_file(file_path, text)
            print("File decrypted successfully.")
        elif enc_mode == 'columnar':
            text = columnar.decrypt(key, content)
            write_file(file_path, text)
            print("File decrypted successfully.")
        else:
            print("Invalid decryption type selected.")
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()
