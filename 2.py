alphabet = "abcdefghijklmnopqrstuvwxyz"

def decimal_to_binary(n):
    binary = ""

    for i in range(8):
        binary = str(n % 2) + binary
        n = n // 2

    return binary


def vigenereCipher(plaintext, key):
    ciphertext = ""

    for i in range(len(plaintext)):
        p=alphabet.index(plaintext[i])
        k = alphabet.index(key[i])

        c = (p+k) % 26

        c_binary = decimal_to_binary(c)
        k_binary = decimal_to_binary(k)

        temp = c_binary[4:]
        c_binary = c_binary[:4] + k_binary[4:]
        k_binary = k_binary[:4] + temp    

        #converting the new binary value of c to decimal
        new_val = 0
        for  bit in c_binary:
            new_val = new_val * 2 + int(bit)

        new_val = new_val % 26

        ciphertext += alphabet[new_val]
    
    return ciphertext
    

plaintext = input("Enter plaintext: ")
key = input("Enter key: ")

cipherText = vigenereCipher(plaintext, key)
print("Ciphertext:", cipherText)