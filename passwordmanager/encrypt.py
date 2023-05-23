import base64
import hashlib
import os
from Crypto.Cipher import AES

class AES256:
    def __init__(self, key):
        # Generate a 256-bit key from the user password
        self.key = hashlib.sha256(key.encode()).digest()
        # Use a random IV for each encryption session
        self.iv = os.urandom(16)

    def encrypt(self, plaintext):
        # Create an AES cipher object with the key and IV
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        # Pad the plaintext to make it a multiple of 16 bytes
        padding_length = 16 - (len(plaintext) % 16)
        plaintext += chr(padding_length) * padding_length
        # Encrypt the plaintext and return the IV and ciphertext in base64
        ciphertext = cipher.encrypt(plaintext.encode())
        return base64.b64encode(self.iv + ciphertext).decode()

    def decrypt(self, ciphertext):
        # Decode the base64-encoded ciphertext
        ciphertext = base64.b64decode(ciphertext)
        # Extract the IV from the first 16 bytes
        iv = ciphertext[:16]
        # Create an AES cipher object with the key and IV
        cipher = AES.new(self.key, AES.MODE_CBC,iv)
        # Decrypt the ciphertext and remove the padding
        plaintext = cipher.decrypt(ciphertext[16:]).decode()
        padding_length = ord(plaintext[-1])
        return plaintext[:-padding_length]