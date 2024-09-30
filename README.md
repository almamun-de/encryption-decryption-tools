# Encryption and Decryption Tools

This project demonstrates two commonly used encryption algorithms: AES (Advanced Encryption Standard) and RSA (Rivest-Shamir-Adleman). The project provides both encryption and decryption tools for protecting sensitive data in transit and at rest.

## Algorithms Implemented
1. **AES (Advanced Encryption Standard)**:
    - Symmetric encryption algorithm (same key is used for both encryption and decryption).
    - Uses CBC mode for encryption.
    - Example usage: Encrypting files, data-at-rest.

2. **RSA (Rivest-Shamir-Adleman)**:
    - Asymmetric encryption algorithm (uses a public key for encryption and a private key for decryption).
    - Example usage: Securing data in transit, exchanging keys securely.

## Requirements
- Python 3.x
- `pycryptodome` library

Install dependencies using the following command:
```bash
pip install -r requirements.txt
