import string
import random

def encrypt_message():
    plain_text = input("Enter a message to encrypt: ")
    cipher_text = ""
    for l in plain_text:
        index = c.index(l)
        cipher_text += key[index]
    print("Original message: ", plain_text)
    print("Encrypted message: ", cipher_text)

def decrypt_message():
    cipher_text = input("Enter a message to decrypt: ")
    plain_text = ""
    for l in cipher_text:
        index = key.index(l)
        plain_text += c[index]
    print("Encrypted message: ", cipher_text)
    print("Original message: ", plain_text)

c = string.digits + string.ascii_letters + string.punctuation + " "
c = list(c)
key = c.copy()
random.shuffle(key)

while True:
    print("\nMenu:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        encrypt_message()
    elif choice == '2':
        decrypt_message()
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
