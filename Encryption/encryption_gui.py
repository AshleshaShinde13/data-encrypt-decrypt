import random
import string
import tkinter as tk
from tkinter import messagebox

def encrypt():
    plain_text = entry_encrypt.get()
    cipher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]

    label_encrypted.config(text="Encrypted message: " + cipher_text)

def decrypt():
    cipher_text = entry_decrypt.get()
    plain_text = ""

    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]

    label_decrypted.config(text="Decrypted message: " + plain_text)

# Initialize the character sets and shuffle the key
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

# Create the main Tkinter window
root = tk.Tk()
root.geometry("600x370")
root.title("Encryption and Decryption")

# Create and place widgets in the window
label_encrypt = tk.Label(root, text="Enter a message to encrypt")
label_encrypt.pack(pady=5)
entry_encrypt = tk.Entry(root, width=50)
entry_encrypt.pack(pady=5)
button_encrypt = tk.Button(root, text="Encrypt", bg="blue", fg="white", command=encrypt)
button_encrypt.pack(pady=5)
label_encrypted = tk.Label(root, text="")
label_encrypted.pack(pady=5)

label_decrypt = tk.Label(root, text="Enter a message to decrypt")
label_decrypt.pack(pady=5)
entry_decrypt = tk.Entry(root, width=50)
entry_decrypt.pack(pady=5)
button_decrypt = tk.Button(root, text="Decrypt", bg="blue", fg="white", command=decrypt)
button_decrypt.pack(pady=5)
label_decrypted = tk.Label(root, text="")
label_decrypted.pack(pady=5)

root.mainloop()
