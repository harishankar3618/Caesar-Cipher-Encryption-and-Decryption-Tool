# Simple Caesar Cipher Encryption and Decryption Tool

This Python script provides a simple implementation of the Caesar cipher for encrypting and decrypting text. The Caesar cipher is a basic encryption technique where each letter in the plaintext is shifted by a certain number of places down the alphabet.

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

The main function of the script which takes user input for the message and the shift value, then performs encryption and decryption, and displays the results.

## Usage

1. Run the script.
2. Enter the message you want to encrypt when prompted.
3. Enter the shift value for the Caesar cipher when prompted.
4. The script will display the encrypted text.
5. The script will then display the decrypted text to show that it matches the original message.

## Example

Enter the message: Hello World
Enter the shift value: 3
Encrypted text: Khoor Zruog
Decrypted text: Hello World

markdown
Copy code

## Notes

- The shift value should be a positive integer.
- The script handles both uppercase and lowercase letters.
- Spaces are preserved in the encrypted and decrypted text.

## Requirements

- Python 3.x

## How to Run

Save the script in a file (e.g., `caesar_cipher.py`) and run it using Python:

```sh
python caesar_cipher.py
