#Encrytion and Decrytion using a key
#Aditya Kumar Roy

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(text, key):
    encrypt_str = ""
    for char in text:
        if char.lower() in alphabet:
            pos = alphabet.index(char.lower())
            new_pos = (pos + key) % 26
            # Preserve case
            if char.isupper():
                encrypt_str += alphabet[new_pos].upper()
            else:
                encrypt_str += alphabet[new_pos]
        else:
            encrypt_str += char
    print("Encrypted message:", encrypt_str)

def decryption(encrypt_str, key):
    decrypt_str = ""
    for char in encrypt_str:
        if char.lower() in alphabet:
            pos = alphabet.index(char.lower())
            new_pos = (pos - key) % 26
            # Preserve case
            if char.isupper():
                decrypt_str += alphabet[new_pos].upper()
            else:
                decrypt_str += alphabet[new_pos]
        else:
            decrypt_str += char
    print("Decrypted message:", decrypt_str)

flag = False
while not flag:
    task = input(r"Type 'encrypt' for encryption and 'decrypt' for decryption: ").lower()
    msg = input("Enter a message: ")
    while True:
        try:
            shift = int(input("Enter the shift key: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    if task == "encrypt":
        encryption(msg, shift)
    elif task == "decrypt":
        decryption(msg, shift)
    else:
        print("Invalid input, please try again.")

    end = input("Type 'yes' to continue and 'no' to end: ").lower()
    if end == "no":
        flag = True