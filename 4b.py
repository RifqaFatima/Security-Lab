3*3 matrix 
################################### NO EUCLIDIAN
alphabet = "abcdefghijklmnopqrstuvwxyz"


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1


def determinant(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[0][2]

    d = matrix[1][0]
    e = matrix[1][1]
    f = matrix[1][2]

    g = matrix[2][0]
    h = matrix[2][1]
    i = matrix[2][2]

    det = a * (e * i - f * h) \
        - b * (d * i - f * g) \
        + c * (d * h - e * g)

    return det


def valid_key(matrix):
    det = determinant(matrix)
    det = det % 26

    return mod_inverse(det, 26) != -1


def matrix_inverse(matrix):
    det = determinant(matrix)
    det = det % 26

    det_inverse = mod_inverse(det, 26)

    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[0][2]

    d = matrix[1][0]
    e = matrix[1][1]
    f = matrix[1][2]

    g = matrix[2][0]
    h = matrix[2][1]
    i = matrix[2][2]

    # Cofactor matrix
    cofactor = [
        [ e*i - f*h, -(d*i - f*g),  d*h - e*g],
        [-(b*i - c*h), a*i - c*g, -(a*h - b*g)],
        [ b*f - c*e, -(a*f - c*d),  a*e - b*d]
    ]

    # Transpose → adjoint
    adjoint = [
        [cofactor[0][0], cofactor[1][0], cofactor[2][0]],
        [cofactor[0][1], cofactor[1][1], cofactor[2][1]],
        [cofactor[0][2], cofactor[1][2], cofactor[2][2]]
    ]

    # Multiply by determinant inverse
    inverse = []

    for row in range(3):
        new_row = []

        for col in range(3):
            value = (adjoint[row][col] * det_inverse) % 26
            new_row.append(value)

        inverse.append(new_row)

    return inverse


def encrypt(plaintext, key):
    ciphertext = ""

    for i in range(0, len(plaintext), 3):

        p = [
            alphabet.index(plaintext[i]),
            alphabet.index(plaintext[i + 1]),
            alphabet.index(plaintext[i + 2])
        ]

        for row in range(3):

            value = 0

            for col in range(3):
                value += key[row][col] * p[col]

            value = value % 26

            ciphertext += alphabet[value]

    return ciphertext


def decrypt(ciphertext, inverse_key):
    plaintext = ""

    for i in range(0, len(ciphertext), 3):

        c = [
            alphabet.index(ciphertext[i]),
            alphabet.index(ciphertext[i + 1]),
            alphabet.index(ciphertext[i + 2])
        ]

        for row in range(3):

            value = 0

            for col in range(3):
                value += inverse_key[row][col] * c[col]

            value = value % 26

            plaintext += alphabet[value]

    return plaintext


# ---------------- MAIN PROGRAM ----------------

key = []

print("Enter 3x3 key matrix:")

for i in range(3):
    row = list(map(int, input().split()))
    key.append(row)


while not valid_key(key):

    print("Invalid key! Matrix does not have an inverse modulo 26.")

    key = []

    print("Enter another 3x3 key matrix:")

    for i in range(3):
        row = list(map(int, input().split()))
        key.append(row)


print("\nValid key matrix.")

plaintext = input("Enter plaintext: ").lower()

# Add x if plaintext length is not a multiple of 3
while len(plaintext) % 3 != 0:
    plaintext += "x"

ciphertext = encrypt(plaintext, key)

inverse_key = matrix_inverse(key)

decrypted = decrypt(ciphertext, inverse_key)

print("Ciphertext:", ciphertext)
print("Decrypted text:", decrypted)


#EUCLIDIAN
alphabet = "abcdefghijklmnopqrstuvwxyz"


# Extended Euclidean Algorithm
def mod_inverse(a, m):

    original_m = m

    # Convert a into the range 0 to m-1
    a = a % m

    # EEA variables
    x0 = 0
    x1 = 1

    while a > 1:

        q = a // m

        a, m = m, a % m
        x0, x1 = x1, x0 - q * x1

    # If gcd(a, m) is not 1,
    # modular inverse does not exist
    if a != 1:
        return -1

    return x1 % original_m


def determinant(matrix):

    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[0][2]

    d = matrix[1][0]
    e = matrix[1][1]
    f = matrix[1][2]

    g = matrix[2][0]
    h = matrix[2][1]
    i = matrix[2][2]

    det = (
        a * (e * i - f * h)
        - b * (d * i - f * g)
        + c * (d * h - e * g)
    )

    return det


def valid_key(matrix):

    # Find determinant
    det = determinant(matrix)

    # Convert determinant to modulo 26
    det = det % 26

    # Check whether determinant has
    # a modular inverse modulo 26
    return mod_inverse(det, 26) != -1


def matrix_inverse(matrix):

    # Find determinant
    det = determinant(matrix)
    det = det % 26

    # Find determinant inverse using EEA
    det_inverse = mod_inverse(det, 26)

    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[0][2]

    d = matrix[1][0]
    e = matrix[1][1]
    f = matrix[1][2]

    g = matrix[2][0]
    h = matrix[2][1]
    i = matrix[2][2]

    # Cofactor matrix
    cofactor = [
        [e * i - f * h, -(d * i - f * g), d * h - e * g],

        [-(b * i - c * h), a * i - c * g, -(a * h - b * g)],

        [b * f - c * e, -(a * f - c * d), a * e - b * d]
    ]

    # Transpose cofactor matrix
    # to get adjoint
    adjoint = [
        [cofactor[0][0], cofactor[1][0], cofactor[2][0]],

        [cofactor[0][1], cofactor[1][1], cofactor[2][1]],

        [cofactor[0][2], cofactor[1][2], cofactor[2][2]]
    ]

    # Calculate inverse matrix
    inverse = []

    for row in range(3):

        new_row = []

        for col in range(3):

            value = (
                adjoint[row][col] * det_inverse
            ) % 26

            new_row.append(value)

        inverse.append(new_row)

    return inverse


def encrypt(plaintext, key):

    ciphertext = ""

    for i in range(0, len(plaintext), 3):

        # Convert letters to numbers
        p = [
            alphabet.index(plaintext[i]),
            alphabet.index(plaintext[i + 1]),
            alphabet.index(plaintext[i + 2])
        ]

        # Matrix multiplication
        for row in range(3):

            value = 0

            for col in range(3):

                value += key[row][col] * p[col]

            value = value % 26

            ciphertext += alphabet[value]

    return ciphertext


def decrypt(ciphertext, inverse_key):

    plaintext = ""

    for i in range(0, len(ciphertext), 3):

        # Convert letters to numbers
        c = [
            alphabet.index(ciphertext[i]),
            alphabet.index(ciphertext[i + 1]),
            alphabet.index(ciphertext[i + 2])
        ]

        # Matrix multiplication
        for row in range(3):

            value = 0

            for col in range(3):

                value += inverse_key[row][col] * c[col]

            value = value % 26

            plaintext += alphabet[value]

    return plaintext


# ---------------- MAIN PROGRAM ----------------

key = []

print("Enter 3x3 key matrix:")

for i in range(3):

    row = list(map(int, input().split()))

    key.append(row)


# Check whether key is valid
while not valid_key(key):

    print("Invalid key!")
    print("Matrix does not have an inverse modulo 26.")

    key = []

    print("Enter another 3x3 key matrix:")

    for i in range(3):

        row = list(map(int, input().split()))

        key.append(row)


print("\nValid key matrix.")

# Read plaintext
plaintext = input("Enter plaintext: ").lower()

# Add x until length is a multiple of 3
while len(plaintext) % 3 != 0:

    plaintext += "x"


# Encrypt
ciphertext = encrypt(plaintext, key)

# Find inverse key using EEA
inverse_key = matrix_inverse(key)

# Decrypt
decrypted = decrypt(ciphertext, inverse_key)


print("Ciphertext:", ciphertext)
print("Decrypted text:", decrypted)