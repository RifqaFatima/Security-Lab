#no eea previous approach.
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# Find modular inverse by checking all values
def mod_inverse(a, m):

    for x in range(1, m):

        if (a * x) % m == 1:
            return x

    return -1


# Calculate determinant of 3x3 matrix
def determinant(key):

    a = key[0][0]
    b = key[0][1]
    c = key[0][2]

    d = key[1][0]
    e = key[1][1]
    f = key[1][2]

    g = key[2][0]
    h = key[2][1]
    i = key[2][2]

    det = a * (e * i - f * h) \
        - b * (d * i - f * g) \
        + c * (d * h - e * g)

    return det


# Check whether key is valid
def valid_key(key):

    det = determinant(key)
    det = det % 26

    return mod_inverse(det, 26) != -1


# Calculate inverse of 3x3 matrix
def matrix_inverse(key):

    det = determinant(key)
    det = det % 26

    det_inverse = mod_inverse(det, 26)

    # Cofactor matrix
    cofactor = [

        [
            key[1][1] * key[2][2] - key[1][2] * key[2][1],
            -(key[1][0] * key[2][2] - key[1][2] * key[2][0]),
            key[1][0] * key[2][1] - key[1][1] * key[2][0]
        ],

        [
            -(key[0][1] * key[2][2] - key[0][2] * key[2][1]),
            key[0][0] * key[2][2] - key[0][2] * key[2][0],
            -(key[0][0] * key[2][1] - key[0][1] * key[2][0])
        ],

        [
            key[0][1] * key[1][2] - key[0][2] * key[1][1],
            -(key[0][0] * key[1][2] - key[0][2] * key[1][0]),
            key[0][0] * key[1][1] - key[0][1] * key[1][0]
        ]

    ]

    # Transpose → adjoint
    adjoint = []

    for i in range(3):

        row = []

        for j in range(3):
            row.append(cofactor[j][i])

        adjoint.append(row)


    # K^-1 = det^-1 × adjoint mod 26
    inverse = []

    for i in range(3):

        row = []

        for j in range(3):

            value = (det_inverse * adjoint[i][j]) % 26

            row.append(value)

        inverse.append(row)

    return inverse


# Extract letters and add X if necessary
def prepare_text(text):

    letters = ""

    for ch in text:

        if ch.isalpha():
            letters += ch.upper()

    while len(letters) % 3 != 0:
        letters += "X"

    return letters


# Encryption
def encrypt(letters, key):

    ciphertext = ""

    for i in range(0, len(letters), 3):

        p1 = alphabet.index(letters[i])
        p2 = alphabet.index(letters[i + 1])
        p3 = alphabet.index(letters[i + 2])


        c1 = (
            key[0][0] * p1 +
            key[0][1] * p2 +
            key[0][2] * p3
        ) % 26


        c2 = (
            key[1][0] * p1 +
            key[1][1] * p2 +
            key[1][2] * p3
        ) % 26


        c3 = (
            key[2][0] * p1 +
            key[2][1] * p2 +
            key[2][2] * p3
        ) % 26


        ciphertext += alphabet[c1]
        ciphertext += alphabet[c2]
        ciphertext += alphabet[c3]

    return ciphertext


# Decryption
def decrypt(ciphertext, inverse_key):

    plaintext = ""

    for i in range(0, len(ciphertext), 3):

        c1 = alphabet.index(ciphertext[i])
        c2 = alphabet.index(ciphertext[i + 1])
        c3 = alphabet.index(ciphertext[i + 2])


        p1 = (
            inverse_key[0][0] * c1 +
            inverse_key[0][1] * c2 +
            inverse_key[0][2] * c3
        ) % 26


        p2 = (
            inverse_key[1][0] * c1 +
            inverse_key[1][1] * c2 +
            inverse_key[1][2] * c3
        ) % 26


        p3 = (
            inverse_key[2][0] * c1 +
            inverse_key[2][1] * c2 +
            inverse_key[2][2] * c3
        ) % 26


        plaintext += alphabet[p1]
        plaintext += alphabet[p2]
        plaintext += alphabet[p3]

    return plaintext


# Restore spaces and punctuation
def restore_text(original, encrypted_letters):

    result = ""
    index = 0

    for ch in original:

        if ch.isalpha():

            result += encrypted_letters[index]
            index += 1

        else:

            result += ch

    return result


# ---------------- MAIN PROGRAM ----------------

plaintext = input("Enter Plaintext: ")


print("\nSelect Key:")
print("1. K1")
print("2. K2")

choice = int(input("Enter choice: "))


K1 = [
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
]


K2 = [
    [2, 4, 12],
    [9, 11, 13],
    [7, 8, 10]
]


if choice == 1:
    key = K1
else:
    key = K2


print("\nKey Matrix:")

for row in key:
    print(row)


# Check key
if not valid_key(key):

    print("\nInvalid Key!")
    print("Determinant has no modular inverse.")
    
else:

    print("\nValid Key!")

    det = determinant(key)
    det_mod = det % 26

    print("Determinant:", det)
    print("Determinant mod 26:", det_mod)

    det_inverse = mod_inverse(det_mod, 26)

    print("Determinant inverse:", det_inverse)


    # Find inverse key
    inverse_key = matrix_inverse(key)

    print("\nInverse Key Matrix:")

    for row in inverse_key:
        print(row)


    # Prepare plaintext
    letters = prepare_text(plaintext)

    print("\nPlaintext letters:", letters)


    # Encryption
    ciphertext_letters = encrypt(letters, key)

    ciphertext = restore_text(
        plaintext,
        ciphertext_letters
    )

    print("Ciphertext:", ciphertext)


    # Decryption
    decrypted_letters = decrypt(
        ciphertext_letters,
        inverse_key
    )

    decrypted = restore_text(
        plaintext,
        decrypted_letters
    )

    print("Decrypted text:", decrypted)