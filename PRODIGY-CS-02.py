"""A simple image encryption and decryption tool using pixel manipulation."""
from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    # Open the image
    image = Image.open(image_path)
    image = image.convert("RGB")
    data = np.array(image)

    # Encrypt the image by applying a basic mathematical operation
    encrypted_data = (data + key) % 256

    # Create and save the encrypted image
    encrypted_image = Image.fromarray(encrypted_data.astype(np.uint8))
    encrypted_image.save("encrypted_image.png")
    print("Image encrypted and saved as encrypted_image.png")

def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_image = encrypted_image.convert("RGB")
    encrypted_data = np.array(encrypted_image)

    # Decrypt the image by reversing the encryption operation
    decrypted_data = (encrypted_data - key) % 256

    # Create and save the decrypted image
    decrypted_image = Image.fromarray(decrypted_data.astype(np.uint8))
    decrypted_image.save("decrypted_image.png")
    print("Image decrypted and saved as decrypted_image.png")

    # Display the decrypted image
    decrypted_image.show()

# Example usage
key = 50  # A simple key for encryption/decryption

# Encrypt the image
encrypt_image("C:\\Users\\sowndarya vathi\\Downloads\\fall-mountain-kc9a0h0ryzzlgj2y.jpg", key) #image path 

# Decrypt the image
decrypt_image("encrypted_image.png", key)
