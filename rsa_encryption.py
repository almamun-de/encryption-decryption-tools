

from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

class RSAEncryption:
    def __init__(self):
        # Generate RSA key pair (public and private)
        self.key = RSA.generate(2048)
        self.public_key = self.key.publickey()

    def encrypt(self, plaintext):
        cipher = PKCS1_OAEP.new(self.public_key)
        ciphertext = cipher.encrypt(plaintext.encode())
        return ciphertext

    def decrypt(self, ciphertext):
        cipher = PKCS1_OAEP.new(self.key)
        plaintext = cipher.decrypt(ciphertext)
        return plaintext.decode()
