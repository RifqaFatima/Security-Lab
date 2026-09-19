alphabet = "abcdefghijklmnopqrstuvwxyz"


def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return -1


def valid_key(key):
    # Determinant
    det = key[0][0] * key[1][1] - key[0][1] * key[1][0]
    det = det % 26

    # Check whether determinant has an inverse modulo 26
    return mod_inverse(det, 26) != -1


def encrypt(plaintext, key):

    plaintext = plaintext.lower()

    text = ""
    for ch in plaintext:
        if ch in alphabet:
            text += ch

    # Add x if length is odd
    if len(text) % 2 != 0:
        text += "x"

    ciphertext = ""

    for i in range(0, len(text), 2):

        p1 = alphabet.index(text[i])
        p2 = alphabet.index(text[i + 1])

        c1 = (key[0][0] * p1 + key[0][1] * p2) % 26
        c2 = (key[1][0] * p1 + key[1][1] * p2) % 26

        ciphertext += alphabet[c1]
        ciphertext += alphabet[c2]

    return ciphertext


def decrypt(ciphertext, key):

    det = key[0][0] * key[1][1] - key[0][1] * key[1][0]
    det = det % 26

    det_inverse = mod_inverse(det, 26)

    # Inverse key matrix
    inverse_key = [
        [(key[1][1] * det_inverse) % 26,
         (-key[0][1] * det_inverse) % 26],

        [(-key[1][0] * det_inverse) % 26,
         (key[0][0] * det_inverse) % 26]
    ]

    plaintext = ""

    for i in range(0, len(ciphertext), 2):

        c1 = alphabet.index(ciphertext[i])
        c2 = alphabet.index(ciphertext[i + 1])

        p1 = (inverse_key[0][0] * c1 +
              inverse_key[0][1] * c2) % 26

        p2 = (inverse_key[1][0] * c1 +
              inverse_key[1][1] * c2) % 26

        plaintext += alphabet[p1]
        plaintext += alphabet[p2]

    return plaintext


# Read key matrix
print("Enter 2x2 key matrix:")

key = []

for i in range(2):
    row = []
    for j in range(2):
        value = int(input("Enter element: "))
        row.append(value)
    key.append(row)


# Check whether key is valid
while not valid_key(key):

    print("Invalid key! The matrix does not have an inverse modulo 26.")
    print("Enter a valid 2x2 key matrix:")

    key = []

    for i in range(2):
        row = []
        for j in range(2):
            value = int(input("Enter element: "))
            row.append(value)
        key.append(row)


plaintext = input("Enter plaintext: ")

ciphertext = encrypt(plaintext, key)
decrypted = decrypt(ciphertext, key)

print("Ciphertext:", ciphertext)
print("Decrypted text:", decrypted)

#EUCLIDIAN
alphabet = "abcdefghijklmnopqrstuvwxyz"


# Extended Euclidean Algorithm
def mod_inverse(a, m):
    original_m = m

    # Make a positive
    a = a % m

    # Extended Euclidean Algorithm
    x0, x1 = 0, 1

    while a > 1:
        q = a // m

        a, m = m, a % m
        x0, x1 = x1, x0 - q * x1

    # If gcd is not 1, inverse does not exist
    if a != 1:
        return -1

    return x1 % original_m


def valid_key(key):

    # Calculate determinant
    det = key[0][0] * key[1][1] - key[0][1] * key[1][0]

    # Convert determinant to modulo 26
    det = det % 26

    # Check whether determinant has an inverse modulo 26
    return mod_inverse(det, 26) != -1


def encrypt(plaintext, key):

    plaintext = plaintext.lower()

    text = ""

    # Remove spaces and non-alphabetic characters
    for ch in plaintext:
        if ch in alphabet:
            text += ch

    # Add x if length is odd
    if len(text) % 2 != 0:
        text += "x"

    ciphertext = ""

    # Encrypt two characters at a time
    for i in range(0, len(text), 2):

        p1 = alphabet.index(text[i])
        p2 = alphabet.index(text[i + 1])

        c1 = (
            key[0][0] * p1 +
            key[0][1] * p2
        ) % 26

        c2 = (
            key[1][0] * p1 +
            key[1][1] * p2
        ) % 26

        ciphertext += alphabet[c1]
        ciphertext += alphabet[c2]

    return ciphertext


def decrypt(ciphertext, key):

    # Calculate determinant
    det = key[0][0] * key[1][1] - key[0][1] * key[1][0]

    # Convert determinant to modulo 26
    det = det % 26

    # Find determinant inverse using EEA
    det_inverse = mod_inverse(det, 26)

    # Calculate inverse key matrix
    inverse_key = [
        [
            (key[1][1] * det_inverse) % 26,
            (-key[0][1] * det_inverse) % 26
        ],
        [
            (-key[1][0] * det_inverse) % 26,
            (key[0][0] * det_inverse) % 26
        ]
    ]

    plaintext = ""

    # Decrypt two characters at a time
    for i in range(0, len(ciphertext), 2):

        c1 = alphabet.index(ciphertext[i])
        c2 = alphabet.index(ciphertext[i + 1])

        p1 = (
            inverse_key[0][0] * c1 +
            inverse_key[0][1] * c2
        ) % 26

        p2 = (
            inverse_key[1][0] * c1 +
            inverse_key[1][1] * c2
        ) % 26

        plaintext += alphabet[p1]
        plaintext += alphabet[p2]

    return plaintext


# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------

# Read key matrix
print("Enter 2x2 key matrix:")

key = []

for i in range(2):

    row = []

    for j in range(2):

        value = int(input("Enter element: "))
        row.append(value)

    key.append(row)


# Check whether key is valid
while not valid_key(key):

    print("\nInvalid key!")
    print("The determinant does not have an inverse modulo 26.")
    print("Therefore, the key matrix cannot be used.")
    print("\nEnter a valid 2x2 key matrix:")

    key = []

    for i in range(2):

        row = []

        for j in range(2):

            value = int(input("Enter element: "))
            row.append(value)

        key.append(row)


# Read plaintext
plaintext = input("\nEnter plaintext: ")


# Encryption
ciphertext = encrypt(plaintext, key)


# Decryption
decrypted = decrypt(ciphertext, key)


# Display results
print("\nCiphertext:", ciphertext)
print("Decrypted text:", decrypted)