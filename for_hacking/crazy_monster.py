import sys
import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidKey

usage_msg = "Usage: " + sys.argv[0] + " (-e/-d) [file] [password]"
help_msg = usage_msg + "\n" + \
           "Examples:\n" + \
           "  To encrypt a file named 'data.txt' with password 'mypassword', do:\n" + \
           "'$ python " + sys.argv[0] + " -e data.txt mypassword'\n" + \
           "  To decrypt the same file, do:\n" + \
           "'$ python " + sys.argv[0] + " -d data.txt.en mypassword'\n"

def derive_key(password, salt):
    """Derive a key from the password and salt using PBKDF2."""
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_file(file_path, password):
    """Encrypt the file at file_path using the provided password."""
    salt = os.urandom(16)
    key = derive_key(password, salt)
    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    with open(file_path, 'rb') as f:
        data = f.read()
    
    encrypted_data = encryptor.update(data) + encryptor.finalize()

    with open(file_path + '.en', 'wb') as f:
        f.write(salt + iv + encrypted_data)

def decrypt_file(file_path, password):
    """Decrypt the file at file_path using the provided password."""
    with open(file_path, 'rb') as f:
        salt = f.read(16)
        iv = f.read(16)
        encrypted_data = f.read()
    
    key = derive_key(password, salt)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    try:
        decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    except InvalidKey:
        print("Invalid password or corrupted file.")
        sys.exit(1)

    original_file_path = file_path.replace('.en', '')
    with open(original_file_path, 'wb') as f:
        f.write(decrypted_data)

if len(sys.argv) != 4:
    print(usage_msg)
    sys.exit(1)

mode = sys.argv[1]
file_path = sys.argv[2]
password = sys.argv[3]

if mode == "-e":
    encrypt_file(file_path, password)
    print(f"File '{file_path}' encrypted to '{file_path}.en'")
elif mode == "-d":
    decrypt_file(file_path, password)
    print(f"File '{file_path}' decrypted.")
elif mode == "-h" or mode == "--help":
    print(help_msg)
else:
    print("Unrecognized first argument: " + mode)
    print("Please use '-e', '-d', or '-h'.")

"""The most important point of this code is the derivation of a cryptographic key from the provided password 
and salt using PBKDF2, which is then used for secure AES encryption and decryption of the file."""
