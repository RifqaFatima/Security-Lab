#Implement monoalphabetic encryption-decryption using the following shift values
#1) k=3(caesar cipher)
#2) k = length of the text

def encrypt(text, k):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    result=""
    for ch in text:
        #if ch in alphabet:
        pos = alphabet.index(ch)
        new_pos = (pos + k)%26
        result += alphabet[new_pos]

    return result

def decrypt(text, k):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result=""
    for ch in text:
        #if ch in alphabet:
        pos = alphabet.index(ch)
        new_pos = (pos - k)%26
        result += alphabet[new_pos]
    
    return result

text = input("Enter your text ")
text = text.replace(" ", "")
k = int(input("Enter your number "))

ciphertext = encrypt(text, k)
print("Encrypted text", ciphertext)

plaintext = decrypt(ciphertext, k)
print("Decrypted text", plaintext)






        











