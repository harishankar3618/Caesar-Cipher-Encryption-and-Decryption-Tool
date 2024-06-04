def encrypt(plaintext, n):
    ans = ""
    # Iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
        # Check if space is there then simply add space
        if ch == " ":
            ans += " "
        # Check if a character is uppercase then encrypt it accordingly
        elif ch.isupper():
            ans += chr((ord(ch) + n - 65) % 26 + 65)
        # Check if a character is lowercase then encrypt it accordingly
        else:
            ans += chr((ord(ch) + n - 97) % 26 + 97)
    return ans


def decrypt(plaintext, n):
    ans = ""
    # Iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
        # Check if space is there then simply add space
        if ch == " ":
            ans += " "
        # Check if a character is uppercase then decrypt it accordingly
        elif ch.isupper():
            ans += chr((ord(ch) - n - 65) % 26 + 65)
        # Check if a character is lowercase then decrypt it accordingly
        else:
            ans += chr((ord(ch) - n - 97) % 26 + 97)
    return ans


def main():
    while True:
        print("\nMenu:")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            text = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_text = encrypt(text, shift)
            print("Encrypted text:", encrypted_text)

        elif choice == '2':
            text = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_text = decrypt(text, shift)
            print("Decrypted text:", decrypted_text)

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


if __name__ == "__main__":
    main()
