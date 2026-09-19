//with numpy nxn
import numpy as np

alphabet = "abcdefghijklmnopqrstuvwxyz"


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1


def valid_key(key):

    det = round(np.linalg.det(key))
    det = det % 26

    return mod_inverse(det, 26) != -1


def matrix_inverse(key):

    det = round(np.linalg.det(key))
    det = det % 26

    det_inverse = mod_inverse(det, 26)

    # Adjugate matrix
    adjoint = np.round(
        np.linalg.det(key) * np.linalg.inv(key)
    ).astype(int)

    # K^-1 = det^-1 × adj(K) mod 26
    inverse = (det_inverse * adjoint) % 26

    return inverse


def encrypt(plaintext, key):

    n = len(key)
    ciphertext = ""

    for i in range(0, len(plaintext), n):

        # Convert characters to numbers
        block = []

        for j in range(n):
            block.append(alphabet.index(plaintext[i + j]))

        block = np.array(block)

        # C = K × P mod 26
        result = np.dot(key, block) % 26

        for value in result:
            ciphertext += alphabet[int(value)]

    return ciphertext


def decrypt(ciphertext, inverse_key):

    n = len(inverse_key)
    plaintext = ""

    for i in range(0, len(ciphertext), n):

        # Convert characters to numbers
        block = []

        for j in range(n):
            block.append(alphabet.index(ciphertext[i + j]))

        block = np.array(block)

        # P = K^-1 × C mod 26
        result = np.dot(inverse_key, block) % 26

        for value in result:
            plaintext += alphabet[int(value)]

    return plaintext


# ---------------- MAIN PROGRAM ----------------

n = int(input("Enter size of key matrix: "))

key = []

print("Enter key matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    key.append(row)

key = np.array(key)


# Check key
while not valid_key(key):

    print("Invalid key! Matrix does not have an inverse modulo 26.")

    key = []

    print("Enter another key matrix:")

    for i in range(n):
        row = list(map(int, input().split()))
        key.append(row)

    key = np.array(key)


print("\nValid key matrix.")

plaintext = input("Enter plaintext: ").lower()

# Make length a multiple of matrix size
while len(plaintext) % n != 0:
    plaintext += "x"


# Encryption
ciphertext = encrypt(plaintext, key)

# Find inverse key
inverse_key = matrix_inverse(key)

# Decryption
decrypted = decrypt(ciphertext, inverse_key)


print("\nKey Matrix:")
print(key)

print("\nInverse Key Matrix:")
print(inverse_key)

print("\nCiphertext:", ciphertext)
print("Decrypted text:", decrypted)

#EUCLIDIAN
# with numpy nxn

import numpy as np

alphabet = "abcdefghijklmnopqrstuvwxyz"


# Extended Euclidean Algorithm
def mod_inverse(a, m):

    original_m = m

    a = a % m

    x0 = 0
    x1 = 1

    while a > 1:

        q = a // m

        a, m = m, a % m
        x0, x1 = x1, x0 - q * x1

    # If gcd is not 1,
    # modular inverse does not exist
    if a != 1:
        return -1

    return x1 % original_m


def valid_key(key):

    det = round(np.linalg.det(key))
    det = det % 26

    # Check whether determinant
    # has an inverse modulo 26
    return mod_inverse(det, 26) != -1


def matrix_inverse(key):

    det = round(np.linalg.det(key))
    det = det % 26

    # Find determinant inverse using EEA
    det_inverse = mod_inverse(det, 26)

    # Adjugate matrix
    adjoint = np.round(
        np.linalg.det(key) * np.linalg.inv(key)
    ).astype(int)

    # K^-1 = det^-1 × adj(K) mod 26
    inverse = (det_inverse * adjoint) % 26

    return inverse


def encrypt(plaintext, key):

    n = len(key)
    ciphertext = ""

    for i in range(0, len(plaintext), n):

        # Convert characters to numbers
        block = []

        for j in range(n):
            block.append(
                alphabet.index(plaintext[i + j])
            )

        block = np.array(block)

        # C = K × P mod 26
        result = np.dot(key, block) % 26

        for value in result:
            ciphertext += alphabet[int(value)]

    return ciphertext


def decrypt(ciphertext, inverse_key):

    n = len(inverse_key)
    plaintext = ""

    for i in range(0, len(ciphertext), n):

        # Convert characters to numbers
        block = []

        for j in range(n):
            block.append(
                alphabet.index(ciphertext[i + j])
            )

        block = np.array(block)

        # P = K^-1 × C mod 26
        result = np.dot(inverse_key, block) % 26

        for value in result:
            plaintext += alphabet[int(value)]

    return plaintext


# ---------------- MAIN PROGRAM ----------------

n = int(input("Enter size of key matrix: "))

key = []

print("Enter key matrix:")

for i in range(n):

    row = list(map(int, input().split()))

    key.append(row)

key = np.array(key)


# Check key
while not valid_key(key):

    print(
        "Invalid key! Matrix does not have "
        "an inverse modulo 26."
    )

    key = []

    print("Enter another key matrix:")

    for i in range(n):

        row = list(map(int, input().split()))

        key.append(row)

    key = np.array(key)


print("\nValid key matrix.")

plaintext = input("Enter plaintext: ").lower()


# Make length a multiple of matrix size
while len(plaintext) % n != 0:
    plaintext += "x"


# Encryption
ciphertext = encrypt(plaintext, key)


# Find inverse key using EEA
inverse_key = matrix_inverse(key)


# Decryption
decrypted = decrypt(ciphertext, inverse_key)


print("\nKey Matrix:")
print(key)

print("\nInverse Key Matrix:")
print(inverse_key)

print("\nCiphertext:", ciphertext)
print("Decrypted text:", decrypted)