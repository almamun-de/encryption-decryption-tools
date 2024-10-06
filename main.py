
from aes_encryption.py import AESEncryption
from rsa_encryption.py import RSAEncryption

def main():
    print("Encryption and Decryption Tool")
    print("1. AES Encryption/Decryption")
    print("2. RSA Encryption/Decryption")
    choice = input("Choose encryption method: ")

    if choice == '1':
        aes_tool = AESEncryption()
        data = input("Enter the data to encrypt using AES: ")
        encrypted_data = aes_tool.encrypt(data)
        print(f"Encrypted (AES): {encrypted_data}")
        decrypted_data = aes_tool.decrypt(encrypted_data)
        print(f"Decrypted (AES): {decrypted_data}")
    elif choice == '2':
        rsa_tool = RSAEncryption()
        data = input("Enter the data to encrypt using RSA: ")
        encrypted_data = rsa_tool.encrypt(data)
        print(f"Encrypted (RSA): {encrypted_data}")
        decrypted_data = rsa_tool.decrypt(encrypted_data)
        print(f"Decrypted (RSA): {decrypted_data}")
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
