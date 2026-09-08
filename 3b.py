Ahh yes — you mean **remove the characters corresponding to the filler `x` positions**, not just remove an `x` from the ciphertext.

For example:

```text
Plaintext:   oop2
Prepared:    oxop2x
```

The filler `x` was inserted at positions **2 and 6**:

```text
o x o p 2 x
↑   ↑     ↑
real filler
```

If encryption gives:

```text
Ciphertext:  abcdex
```

you want to remove the ciphertext characters corresponding to those filler positions too.

### Best way

Keep track of which positions contain filler `x` while preparing the plaintext.

Modify `prepare_text()` like this:

```python
def prepare_text(text):
    text = text.lower()

    clean = ""
    for ch in text:
        if ch in characters:
            clean += ch

    prepared = ""
    filler_positions = []

    i = 0
    while i < len(clean):
        first = clean[i]

        if i + 1 == len(clean):
            prepared += first + "x"
            filler_positions.append(len(prepared) - 1)
            i += 1

        elif clean[i] == clean[i + 1]:
            prepared += first + "x"
            filler_positions.append(len(prepared) - 1)
            i += 1

        else:
            prepared += clean[i] + clean[i + 1]
            i += 2

    return prepared, filler_positions
```

Then in your main program:

```python
prepared, filler_positions = prepare_text(plaintext)

ciphertext = encrypt(prepared, matrix)
decrypted = decrypt(ciphertext, matrix)

# Remove filler positions from ciphertext and decrypted text
final_ciphertext = ""
final_decrypted = ""

for i in range(len(ciphertext)):
    if i not in filler_positions:
        final_ciphertext += ciphertext[i]
        final_decrypted += decrypted[i]

print("Prepared plaintext:", prepared)
print("Ciphertext:", final_ciphertext)
print("Decrypted text:", final_decrypted)
```

### For your example

```text
Plaintext       = oop2
Prepared        = oxop2x
Filler positions = 1, 5
```

So:

```text
Prepared:    o x o p 2 x
             ↑       ↑
           remove  remove
```

And the **same positions** are removed from both:

```text
Ciphertext:  A B C D E F
                ↑       ↑
              remove  remove

Decrypted:   o x o p 2 x
                ↑       ↑
              remove  remove
```

Result:

```text
Ciphertext:  ACDE
Decrypted:   oop2
```

This is the correct approach because the `x` itself **doesn't necessarily appear in the ciphertext** — you need to remember its **position**.
