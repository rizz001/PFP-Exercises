def alphabet_position(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    positions = [str(alphabet.find(c) + 1) for c in text.lower() if c in alphabet]
    return " ".join(positions)

result = alphabet_position("Hello")
print(result)