alphabet = "abcdefghijklmnopqrstuvwxyz"


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1


def determinant(matrix):
    n = len(matrix)

    # 1x1 matrix
    if n == 1:
        return matrix[0][0]

    # 2x2 matrix
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0

    for col in range(n):

        # Create smaller matrix
        submatrix = []

        for row in range(1, n):
            new_row = []

            for j in range(n):
                if j != col:
                    new_row.append(matrix[row][j])

            submatrix.append(new_row)

        # Cofactor
        sign = (-1) ** col

        det += sign * matrix[0][col] * determinant(submatrix)

    return det


def valid_key(matrix):

    det = determinant(matrix)

    # Work modulo 26
    det = det % 26

    # Determinant must have a modular inverse
    return mod_inverse(det, 26) != -1


def matrix_inverse(matrix):

    n = len(matrix)

    det = determinant(matrix)
    det = det % 26

    det_inverse = mod_inverse(det, 26)

    # Find cofactors
    cofactor_matrix = []

    for row in range(n):

        cofactor_row = []

        for col in range(n):

            submatrix = []

            for i in range(n):
                if i == row:
                    continue

                new_row = []

                for j in range(n):
                    if j == col:
                        continue

                    new_row.append(matrix[i][j])

                submatrix.append(new_row)

            cofactor = ((-1) ** (row + col)) * determinant(submatrix)

            cofactor_row.append(cofactor)

        cofactor_matrix.append(cofactor_row)

    # Transpose cofactor matrix
    adjoint = []

    for row in range(n):
        new_row = []

        for col in range(n):
            new_row.append(cofactor_matrix[col][row])

        adjoint.append(new_row)

    # Multiply by determinant inverse
    inverse = []

    for row in range(n):

        new_row = []

        for col in range(n):

            value = (adjoint[row][col] * det_inverse) % 26

            new_row.append(value)

        inverse.append(new_row)

    return inverse


def encrypt(plaintext, key):

    n = len(key)
    ciphertext = ""

    for i in range(0, len(plaintext), n):

        # Convert block into numbers
        block = []

        for j in range(n):
            block.append(alphabet.index(plaintext[i + j]))

        # Matrix multiplication
        for row in range(n):

            value = 0

            for col in range(n):
                value += key[row][col] * block[col]

            value = value % 26

            ciphertext += alphabet[value]

    return ciphertext


def decrypt(ciphertext, inverse_key):

    n = len(inverse_key)
    plaintext = ""

    for i in range(0, len(ciphertext), n):

        # Convert block into numbers
        block = []

        for j in range(n):
            block.append(alphabet.index(ciphertext[i + j]))

        # Matrix multiplication
        for row in range(n):

            value = 0

            for col in range(n):
                value += inverse_key[row][col] * block[col]

            value = value % 26

            plaintext += alphabet[value]

    return plaintext


# ---------------- MAIN PROGRAM ----------------

n = int(input("Enter size of key matrix: "))

key = []

print("Enter key matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    key.append(row)


# Check whether key is valid
while not valid_key(key):

    print("Invalid key! Matrix does not have an inverse modulo 26.")

    key = []

    print("Enter another key matrix:")

    for i in range(n):
        row = list(map(int, input().split()))
        key.append(row)


print("\nValid key matrix.")

plaintext = input("Enter plaintext: ").lower()

# Add x until length is a multiple of n
while len(plaintext) % n != 0:
    plaintext += "x"


# Encryption
ciphertext = encrypt(plaintext, key)

# Find inverse key
inverse_key = matrix_inverse(key)

# Decryption
decrypted = decrypt(ciphertext, inverse_key)


print("\nCiphertext:", ciphertext)
print("Decrypted text:", decrypted)

#EUCLIDIAN
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

    # If gcd is not 1, inverse does not exist
    if a != 1:
        return -1

    return x1 % original_m


def determinant(matrix):

    n = len(matrix)

    # 1x1 matrix
    if n == 1:
        return matrix[0][0]

    # 2x2 matrix
    if n == 2:
        return (
            matrix[0][0] * matrix[1][1]
            - matrix[0][1] * matrix[1][0]
        )

    det = 0

    for col in range(n):

        # Create smaller matrix
        submatrix = []

        for row in range(1, n):

            new_row = []

            for j in range(n):

                if j != col:
                    new_row.append(matrix[row][j])

            submatrix.append(new_row)

        # Cofactor sign
        sign = (-1) ** col

        det += sign * matrix[0][col] * determinant(submatrix)

    return det


def valid_key(matrix):

    det = determinant(matrix)

    # Work modulo 26
    det = det % 26

    # Determinant must have a modular inverse
    return mod_inverse(det, 26) != -1


def matrix_inverse(matrix):

    n = len(matrix)

    det = determinant(matrix)
    det = det % 26

    # Find determinant inverse using EEA
    det_inverse = mod_inverse(det, 26)

    # Find cofactors
    cofactor_matrix = []

    for row in range(n):

        cofactor_row = []

        for col in range(n):

            submatrix = []

            for i in range(n):

                if i == row:
                    continue

                new_row = []

                for j in range(n):

                    if j == col:
                        continue

                    new_row.append(matrix[i][j])

                submatrix.append(new_row)

            cofactor = (
                (-1) ** (row + col)
            ) * determinant(submatrix)

            cofactor_row.append(cofactor)

        cofactor_matrix.append(cofactor_row)

    # Transpose cofactor matrix
    # to get adjoint
    adjoint = []

    for row in range(n):

        new_row = []

        for col in range(n):

            new_row.append(
                cofactor_matrix[col][row]
            )

        adjoint.append(new_row)

    # Multiply adjoint by determinant inverse
    inverse = []

    for row in range(n):

        new_row = []

        for col in range(n):

            value = (
                adjoint[row][col] * det_inverse
            ) % 26

            new_row.append(value)

        inverse.append(new_row)

    return inverse


def encrypt(plaintext, key):

    n = len(key)

    ciphertext = ""

    for i in range(0, len(plaintext), n):

        # Convert block into numbers
        block = []

        for j in range(n):

            block.append(
                alphabet.index(plaintext[i + j])
            )

        # Matrix multiplication
        for row in range(n):

            value = 0

            for col in range(n):

                value += (
                    key[row][col] * block[col]
                )

            value = value % 26

            ciphertext += alphabet[value]

    return ciphertext


def decrypt(ciphertext, inverse_key):

    n = len(inverse_key)

    plaintext = ""

    for i in range(0, len(ciphertext), n):

        # Convert block into numbers
        block = []

        for j in range(n):

            block.append(
                alphabet.index(ciphertext[i + j])
            )

        # Matrix multiplication
        for row in range(n):

            value = 0

            for col in range(n):

                value += (
                    inverse_key[row][col] * block[col]
                )

            value = value % 26

            plaintext += alphabet[value]

    return plaintext


# ---------------- MAIN PROGRAM ----------------

n = int(input("Enter size of key matrix: "))

key = []

print("Enter key matrix:")

for i in range(n):

    row = list(map(int, input().split()))

    key.append(row)


# Check whether key is valid
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


print("\nValid key matrix.")

plaintext = input("Enter plaintext: ").lower()

# Add x until length is a multiple of n
while len(plaintext) % n != 0:

    plaintext += "x"


# Encryption
ciphertext = encrypt(plaintext, key)


# Find inverse key using EEA
inverse_key = matrix_inverse(key)


# Decryption
decrypted = decrypt(ciphertext, inverse_key)


print("\nCiphertext:", ciphertext)
print("Decrypted text:", decrypted)