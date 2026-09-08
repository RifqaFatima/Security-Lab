alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def extended_vigenere(plaintext, key):
    ciphertext = ""

    for i in range(len(plaintext)):
        # A=0, B=1, ..., Z=25
        p = alphabet.index(plaintext[i].upper())
        k = alphabet.index(key[i % len(key)].upper())

        # Vigenere encryption
        c = (p + k) % 26

        # Convert C and key to 8-bit binary
        c_binary = format(c, '08b')
        k_binary = format(k, '08b') 

        # Swap lower 4 bits
        new_binary = c_binary[:4] + k_binary[4:]

        # Binary to decimal
        new_value = int(new_binary, 2)

        # Wrap around to 0-25
        new_value = new_value % 26

        # Convert number back to character
        ciphertext += alphabet[new_value]

    return ciphertext


plaintext = input("Enter Plaintext: ")
key = input("Enter Key: ")

ciphertext = extended_vigenere(plaintext, key)

print("Ciphertext:", ciphertext)