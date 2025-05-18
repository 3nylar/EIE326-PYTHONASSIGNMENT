# Caesar Cipher

def caesar_cipher(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            # Preserve case
            start = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - start + shift) % 26 + start
            encrypted += chr(shifted)
        else:
            encrypted += char  
    return encrypted

message = input("Enter the message: ")
shift_value = int(input("Enter shift value (e.g., 3): "))

ciphered_text = caesar_cipher(message, shift_value)
print("Encrypted message:", ciphered_text)
