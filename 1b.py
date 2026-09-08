alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(text, k):
    result = ""

    for ch in text:
        if ch in alphabet:
            pos = alphabet.index(ch)
            result += alphabet[(pos + k) % 26]

    return result


def decrypt(text, k):
    result = ""

    for ch in text:
        if ch in alphabet:
            pos = alphabet.index(ch)
            result += alphabet[(pos - k) % 26]

    return result


text = input("Enter text: ")

# Remove spaces
text = text.replace(" ", "")

# i) k = 3
k = 3
encrypted = encrypt(text, k)
print("Encrypted (k=3):", encrypted)
print("Decrypted:", decrypt(encrypted, k))


# ii) k = length of text
k = len(text)
encrypted = encrypt(text, k)
print("Encrypted (k=length):", encrypted)
print("Decrypted:", decrypt(encrypted, k))