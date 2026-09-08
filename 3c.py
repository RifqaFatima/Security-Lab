characters = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_+"


def create_matrix(key):
    key = key.lower()

    letters = ""

    # Add key characters without repetition
    for ch in key:
        if ch in characters and ch not in letters:
            letters += ch

    # Add remaining characters
    for ch in characters:
        if ch not in letters:
            letters += ch

    # Create 7 x 7 matrix
    matrix = []

    for i in range(0, 49, 7):
        matrix.append(letters[i:i+7])

    return matrix


def prepare_text(text):
    text = text.lower()

    clean = ""

    for ch in text:
        if ch in characters:
            clean += ch

    prepared = ""
    i = 0

    while i < len(clean):

        first = clean[i]

        # Last character
        if i + 1 == len(clean):
            prepared += first + "x"
            i += 1

        # Repeated characters
        elif clean[i] == clean[i + 1]:
            prepared += first + "x"
            i += 1

        else:
            prepared += clean[i] + clean[i + 1]
            i += 2

    return prepared


def find_position(matrix, ch):

    for row in range(7):
        for col in range(7):

            if matrix[row][col] == ch:
                return row, col


def encrypt(plaintext, matrix):

    ciphertext = ""

    for i in range(0, len(plaintext), 2):

        a = plaintext[i]
        b = plaintext[i + 1]

        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        # Same row
        if r1 == r2:

            ciphertext += matrix[r1][(c1 + 1) % 7]
            ciphertext += matrix[r2][(c2 + 1) % 7]

        # Same column
        elif c1 == c2:

            ciphertext += matrix[(r1 + 1) % 7][c1]
            ciphertext += matrix[(r2 + 1) % 7][c2]

        # Rectangle rule
        else:

            ciphertext += matrix[r1][c2]
            ciphertext += matrix[r2][c1]

    return ciphertext


def decrypt(ciphertext, matrix):

    plaintext = ""

    for i in range(0, len(ciphertext), 2):

        a = ciphertext[i]
        b = ciphertext[i + 1]

        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        # Same row
        if r1 == r2:

            plaintext += matrix[r1][(c1 - 1) % 7]
            plaintext += matrix[r2][(c2 - 1) % 7]

        # Same column
        elif c1 == c2:

            plaintext += matrix[(r1 - 1) % 7][c1]
            plaintext += matrix[(r2 - 1) % 7][c2]

        # Rectangle rule
        else:

            plaintext += matrix[r1][c2]
            plaintext += matrix[r2][c1]

    return plaintext


# Main program

key = input("Enter key: ")
plaintext = input("Enter plaintext: ")

matrix = create_matrix(key)

print("\nPlayfair Matrix:")

for row in matrix:
    print(" ".join(row))

prepared = prepare_text(plaintext)

print("\nPrepared plaintext:", prepared)

ciphertext = encrypt(prepared, matrix)

print("Ciphertext:", ciphertext)

decrypted = decrypt(ciphertext, matrix)

print("Decrypted text:", decrypted)