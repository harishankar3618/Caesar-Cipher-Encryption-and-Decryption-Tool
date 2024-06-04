
# Simple Caesar Cipher Encryption and Decryption Tool

This Python script provides a simple menu-driven implementation of the Caesar cipher for encrypting and decrypting text. The Caesar cipher is a basic encryption technique where each letter in the plaintext is shifted by a certain number of places down the alphabet.

## Overview

The script contains functions for encrypting and decrypting text using the Caesar cipher, as well as a main function that provides a menu-driven interface for the user. The user can choose to encrypt text, decrypt text, or exit the program.

## Functions

### `encrypt(plaintext, n)`

Encrypts the given plaintext using the Caesar cipher.

- `plaintext`: The text to be encrypted.
- `n`: The shift value for the Caesar cipher.

The function iterates over each character in the plaintext, checks if it is a space, uppercase, or lowercase letter, and applies the appropriate encryption logic. Spaces remain unchanged.

### `decrypt(plaintext, n)`

Decrypts the given ciphertext using the Caesar cipher.

- `plaintext`: The text to be decrypted.
- `n`: The shift value that was used during encryption.

The function iterates over each character in the ciphertext, checks if it is a space, uppercase, or lowercase letter, and applies the appropriate decryption logic. Spaces remain unchanged.

## Main Function

### `main()`

The main function of the script provides a menu-driven interface to the user. It prompts the user to choose an action (encrypt, decrypt, or exit) and performs the corresponding operation.

## Usage

1. Run the script.
2. Follow the menu prompts to:
   - Encrypt text: Enter the message and the shift value to get the encrypted text.
   - Decrypt text: Enter the encrypted message and the shift value to get the decrypted text.
   - Exit the program.

## Notes

- The shift value should be a positive integer.
- The script handles both uppercase and lowercase letters.
- Spaces are preserved in the encrypted and decrypted text.

## Requirements

- Python 3.x

## License

This code is provided as-is without any warranty. You are free to use, modify, and distribute it as you see fit.
