
characters = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_+"

def create_matrix(key):
    letters = ""

    #removing repeated key characters
    for ch in key:
        if ch.isalpha() and ch not in letters:
            letters += ch

    #add the remaining char
    for ch in characters:
        if ch not in letters:
            letters += ch

    #7x7 matrix
    matrix = []

    for i in range (0, 49, 7): #i: 0, 7, 14, 21, 28, 35, 42
        matrix.append(list(letters[i:i+7]))
    return matrix

def modify_matrix(matrix, key):
    #ascii sum of key
    total = 0

    for ch in key.lower():
            if ch in characters:
                total += ord(ch)
    print("ASCII Sum:", total)

    #sum is odd --> revers the columns
    if total % 2 == 1:

        for row in matrix:
            row.reverse()

    #sum is even --> reverse the rowss
    else:
        matrix.reverse()

    return matrix

filler = []

def prepare_text(text):
    text = text.lower()

    prepared = ""
    i = 0
    
    while i < len(text):

        first = text[i]

        #Last character
        if i + 1 == len(text):
            prepared += first + "x"
            filler.append(len(prepared) - 1)
            i += 1

        # Repeated characters
        elif text[i] == text[i + 1]:
            prepared += first + "x"
            filler.append(len(prepared) - 1)
            i += 1

        else:
            prepared += text[i] + text[i + 1]
            i += 2

    return prepared

def find_position(matrix, ch):

    for row in range(7):
        for col in range(7):

            if matrix[row][col] == ch:
                return row, col



def encrypt(prepared, matrix):

    ciphertext = ""

    for i in range(0, len(prepared), 2):

        a = prepared[i]
        b = prepared[i + 1]


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


key = input("Enter key: ")
plaintext = input("Enter plaintext: ")

matrix = create_matrix(key)

print("\nOriginal Playfair Matrix: ")
for row in matrix:
    print(" ".join(row))

matrix = modify_matrix(matrix, key)

print("\nModified Playfair Matrix: ")
for row in matrix:
    print(" ".join(row))

prepared = prepare_text(plaintext)


final_ciphertext = ""
final_decrypted = ""


ciphertext = encrypt(prepared, matrix)

decrypted = decrypt(ciphertext, matrix)

for i in range(len(ciphertext)):
    if i not in filler:
        final_ciphertext += ciphertext[i]
        final_decrypted += decrypted[i]

print("Prepared plaintext:", prepared)
print("Ciphertext:", final_ciphertext)
print("Decrypted text:", final_decrypted)

