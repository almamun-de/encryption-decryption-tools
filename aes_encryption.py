from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

class AESEncryption:
    def __init__(self, key_size=32):
        self.key = get_random_bytes(key_size)  # Generate a random AES key (256-bit)

    def encrypt(self, plaintext):
        cipher = AES.new(self.key, AES.MODE_CBC)  # CBC mode
        iv = cipher.iv
        ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
        return iv + ciphertext  # Return IV + ciphertext

    def decrypt(self, ciphertext):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size)
        return plaintext.decode()

