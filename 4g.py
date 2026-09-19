#with numpy
import numpy as np

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# Extended Euclidean Algorithm
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y


# Modular inverse using EEA
def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)

    if gcd != 1:
        return -1

    return x % m


# Check whether key has an inverse modulo 26
def valid_key(key):

    det = round(np.linalg.det(key))
    det = det % 26

    return mod_inverse(det, 26) != -1


# Find inverse key matrix
def matrix_inverse(key):

    det = round(np.linalg.det(key))
    det = det % 26

    det_inverse = mod_inverse(det, 26)

    # Adjoint matrix
    adjoint = np.round(
        np.linalg.det(key) * np.linalg.inv(key)
    ).astype(int)

    inverse_key = (det_inverse * adjoint) % 26

    return inverse_key


# Extract only letters and remember positions
def prepare_text(text):

    letters = ""

    for ch in text:
        if ch.isalpha():
            letters += ch.upper()

    while len(letters) % 3 != 0:
        letters += "X"

    return letters


# Put encrypted/decrypted letters back into
# their original positions
def restore_text(original, encrypted_letters):

    result = ""
    index = 0

    for ch in original:

        if ch.isalpha():
            result += encrypted_letters[index]
            index += 1

        else:
            result += ch

    # If padding X was added, don't display it
    # because it was not present in the original text

    return result


# Encryption
def encrypt(plaintext, key):

    plaintext_letters = prepare_text(plaintext)

    ciphertext = ""

    for i in range(0, len(plaintext_letters), 3):

        trigram = plaintext_letters[i:i+3]

        P = []

        for ch in trigram:
            P.append(alphabet.index(ch))

        P = np.array(P)

        # C = K × P mod 26
        C = np.dot(key, P) % 26

        for value in C:
            ciphertext += alphabet[int(value)]

    return ciphertext


# Decryption
def decrypt(ciphertext, inverse_key):

    plaintext = ""

    for i in range(0, len(ciphertext), 3):

        trigram = ciphertext[i:i+3]

        C = []

        for ch in trigram:
            C.append(alphabet.index(ch))

        C = np.array(C)

        # P = K^-1 × C mod 26
        P = np.dot(inverse_key, C) % 26

        for value in P:
            plaintext += alphabet[int(value)]

    return plaintext


# ------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------

plaintext = input("Enter Plaintext: ")

print("\nSelect Key:")
print("1. K1")
print("2. K2")

choice = int(input("Enter choice: "))


K1 = np.array([
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
])

K2 = np.array([
    [2, 4, 12],
    [9, 11, 13],
    [7, 8, 10]
])


if choice == 1:
    key = K1
else:
    key = K2


print("\nKey Matrix:")
print(key)


# Validate key
if not valid_key(key):

    print("\nInvalid key!")
    print("Determinant does not have an inverse modulo 26.")

else:

    print("\nValid key!")

    determinant = round(np.linalg.det(key))
    determinant_mod = determinant % 26

    print("Determinant:", determinant)
    print("Determinant mod 26:", determinant_mod)

    det_inverse = mod_inverse(determinant_mod, 26)

    print("Determinant inverse:", det_inverse)

    inverse_key = matrix_inverse(key)

    print("\nInverse Key Matrix:")
    print(inverse_key)

    # Get only letters
    letters = prepare_text(plaintext)

    print("\nPlaintext letters:", letters)

    # Encryption
    ciphertext_letters = encrypt(plaintext, key)

    # Put spaces and punctuation back
    ciphertext = restore_text(plaintext, ciphertext_letters)

    print("Ciphertext:", ciphertext)

    # Decryption
    decrypted_letters = decrypt(ciphertext_letters, inverse_key)

    # Put spaces and punctuation back
    decrypted = restore_text(plaintext, decrypted_letters)

    print("Decrypted text:", decrypted)