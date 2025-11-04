# Ciphers

A small, educational collection of classical cipher implementations in Python. The repository contains straightforward, self‑contained implementations intended for learning, experimentation, and small utilities for file encryption/decryption.

Description
- This repo implements common classical ciphers with simple interfaces:
  - Caesar cipher (shift)
  - Columnar transposition cipher
  - Columnar + Caesar (Colsar)
  - Multiplication cipher
  - Affine cipher (Multiplication + Shift)
- Implementations prioritize readability and simplicity over performance or cryptographic security.
- Useful for learning, teaching, quick experiments, and small text-based puzzles.

Repository layout
- affine.py — MultiplicationCipher and AffineCipher implementations.
- caesar.py — CaesarCipher implementation.
- columnar.py — ColumnarCipher (columnar transposition) implementation.
- columnar_caesar.py — ColsarCipher that composes Columnar + Caesar.
- fileEncryptor.py — Simple CLI that reads/writes files and applies the ciphers.

Caveats and safety
- These are educational implementations of classical ciphers and are NOT secure for any real-world confidentiality needs.
- The symbol set used by the ciphers includes lowercase letters, digits, and many punctuation characters. Uppercase text will be treated as different characters (see examples).
- Keys are simple integers; some ciphers require co-prime keys (see details below).

Details: algorithms & how to use them
All ciphers use the same symbol alphabet defined in their classes:
abcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()_-+={}[]|\:;\"\'<>,.?/Δƒ€ŠŒ©®§

1) CaesarCipher (caesar.py)
- Shift-based substitution: each character index is shifted by key modulo alphabet length.
- Methods:
  - encrypt(text, key) — returns ciphertext
  - decrypt(text, key) — returns plaintext
- Constraints: if key > alphabet length the method returns an error message.

Example:
from caesar import CaesarCipher
c = CaesarCipher()
ct = c.encrypt("hello world", 3)
pt = c.decrypt(ct, 3)

2) ColumnarCipher (columnar.py)
- Columnar transposition: plaintext is written in rows with given key (number of columns) and read column-by-column.
- Methods:
  - encrypt(key, text) — returns ciphertext
  - decrypt(key, ciphertext) — returns plaintext
- Constraints: key must be >= 2 and less than the text length.

Example:
from columnar import ColumnarCipher
col = ColumnarCipher()
ct = col.encrypt(5, "attackatdawn")
pt = col.decrypt(5, ct)

3) ColsarCipher (columnar_caesar.py)
- Composition of Caesar and Columnar:
  - Encryption: Caesar encrypts first with provided key; then a columnar key is derived from the Caesar key and the length of the Caesar ciphertext and used to columnar-encrypt that result.
  - Decryption: reverses the operations (columnar decrypt first, then Caesar decrypt).
- Methods:
  - encrypt(text, key)
  - decrypt(cipher, key)
- Note: columnar key is computed as int((key * key) % (len(text) / 2)) — this is arbitrary and intended for demonstration.

4) MultiplicationCipher (affine.py)
- Multiplicative cipher: maps character index x to (k * x) mod m, where m is the alphabet length.
- Methods:
  - encrypt(text, key) — key must be co-prime with alphabet length; otherwise an error message is returned.
  - decrypt(cipher, key) — uses modular inverse of key with respect to alphabet length to recover plaintext.
- The class contains:
  - gcd(a, b) — greatest common divisor
  - modularInverse(key, symbol) — multiplicative inverse using extended Euclidean algorithm

5) AffineCipher (affine.py)
- Affine cipher: combination of multiplication and shift: E(x) = (a*x + b) mod m
- Methods:
  - encrypt(text, key, key2) — key (a) must be co-prime with alphabet length; key2 (b) is the additive shift.
  - decrypt(cipher, key, key2) — recovers plaintext using modular inverse of a.
- Uses same helpers (gcd and modularInverse) as MultiplicationCipher.

fileEncryptor.py — simple CLI
- Interactive program to encrypt or decrypt files using any of the included ciphers.
- Prompts for:
  - file path
  - mode (e or d)
  - encryption algorithm name (one of: caesar, columnar, colsar, multiplication, affine)
  - key(s)
- Reads the entire file as UTF-8 text, transforms it, and overwrites the same file with the result.
- Use with caution: it overwrites the input file.

Quick usage examples
- Encrypt a string with Caesar:
  python -c "from caesar import CaesarCipher; print(CaesarCipher().encrypt('hello',3))"

- Run the file encryptor:
  python fileEncryptor.py
  Follow prompts to select mode, algorithm, and keys.

Notes on behavior and potential improvements
- Symbol set is lowercase-only. If you want case-insensitive behavior or to support uppercase letters equally, convert input to the desired case before encryption or extend the symbol alphabet.
- fileEncryptor overwrites files in place. Add an option to write to a separate output file to avoid accidental data loss.
- Input validation: some functions currently return error messages as strings (e.g., when keys are invalid). Consider raising exceptions or using consistent return types.
- Tests: there are no automated tests included. Adding unit tests (pytest) would make the project easier to maintain.
- Packaging: the code is pure Python and requires no external dependencies.

Contributing
- Contributions are welcome. Good first contributions:
  - Add unit tests for each cipher.
  - Add more ciphers (e.g., Vigenère, Playfair).
  - Add options to fileEncryptor to write to new files and to select symbol alphabets.
  - Make the CLI accept command-line arguments (argparse) and add a --dry-run mode.
- Please follow simple guidelines:
  - Keep implementations readable, well-documented, and accompanied by examples and tests.
  - Open pull requests with a clear description and small, focused changes.


Author / Maintainer
- @paulfruitful
