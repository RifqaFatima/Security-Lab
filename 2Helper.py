def extended_vigenere(plaintext, key):
    ciphertext = ""

    for i in range(len(plaintext)):
        # Convert plaintext and key characters to ASCII values
        p = ord(plaintext[i])
        k = ord(key[i % len(key)])

        # Vigenere encryption
        c = (p + k) % 256

        # Convert C and key to 8-bit binary
        c_binary = format(c, '08b')
        k_binary = format(k, '08b')

        # Swap lower 4 bits
        new_c_binary = c_binary[:4] + k_binary[4:]

        # Convert binary back to integer
        new_c = int(new_c_binary, 2)

        # Convert integer to character
        ciphertext += chr(new_c)

    return ciphertext


plaintext = input("Enter Plaintext: ")
key = input("Enter Key: ")

ciphertext = extended_vigenere(plaintext, key)

print("Ciphertext:", ciphertext)