from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher = Fernet(key)

print(f"KEY: {key.decode()}")  # Save this somewhere safe

# Encrypt
with open("secret.txt", "rb") as file:
    original = file.read()

encrypted = cipher.encrypt(original)
with open("encrypted.txt", "wb") as file:
    file.write(encrypted)

# Decrypt
decrypted = cipher.decrypt(encrypted)
print("Decrypted content:", decrypted.decode())
