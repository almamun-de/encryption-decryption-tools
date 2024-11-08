# Encryption and Decryption Tools

This project demonstrates two commonly used encryption algorithms: AES (Advanced Encryption Standard) and RSA (Rivest-Shamir-Adleman). The project provides both encryption and decryption tools for protecting sensitive data in transit and at rest.

## Alg

Install dependencies using the following command:
```bash
pip install -r requirements.txt
```

AES Encryption/Decryption
AES is a symmetric key encryption algorithm where the same key is used for both encryption and decryption.
```bash
aes_tool = AESEncryption()
encrypted_data = aes_tool.encrypt("Sensitive data")
decrypted_data = aes_tool.decrypt(encrypted_data)
```

RSA Encryption/Decryption
RSA is an asymmetric key encryption algorithm. You encrypt the data with a public key, and it can only be decrypted using the corresponding private key.
```bash
rsa_tool = RSAEncryption()
encrypted_data = rsa_tool.encrypt("Sensitive data")
decrypted_data = rsa_tool.decrypt(encrypted_data)
```
