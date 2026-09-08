alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def extended_vigenere(plaintext, key):
    ciphertext = ""

    for i in range(len(plaintext)):
        # A=1, B=2, ..., Z=26
        p = alphabet.index(plaintext[i].upper()) + 1
        k = alphabet.index(key[i % len(key)].upper()) + 1

        # Vigenere encryption
        c = (p + k) % 26

        if c == 0:
            c = 26

        # Convert C and key to 8-bit binary
        c_binary = format(c, '08b')
        k_binary = format(k, '08b')

        # Swap lower 4 bits
        new_binary = c_binary[:4] + k_binary[4:]

        # Binary to decimal
        new_value = int(new_binary, 2)

        # Wrap around to 1-26
        new_value = ((new_value - 1) % 26) + 1

        # Convert number back to character
        ciphertext += alphabet[new_value - 1]

    return ciphertext


plaintext = input("Enter Plaintext: ")
key = input("Enter Key: ")

ciphertext = extended_vigenere(plaintext, key)

print("Ciphertext:", ciphertext)