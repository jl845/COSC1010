#
# Jordyn Luna
# 11/24/2024
# File Encryption and Decryption Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

def main():
    # Create a dictionary with codes for encryption
    codes = {'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '$', 'c': '3', 'D': 'q', 'd': '7', 
             'E': '^', 'e': '1', 'F': '&', 'f': '*', 'G': '2', 'g': '0', 'H': '(', 'h': '4', 
             'I': ')', 'i': '5', 'J': '-', 'j': '6', 'K': '_', 'k': '8', 'L': '=', 'l': '!', 
             'M': '+', 'm': 'w', 'N': '[', 'n': 'r', 'O': ']', 'o': 't', 'P': '{', 'p': 'u', 
             'Q': 'd', 'q': 'v', 'R': '<', 'r': 'x', 'S': '>', 's': 'y', 'T': '?', 't': 'z', 
             'U': '/', 'u': 'a', 'V': '\\', 'v': 'b', 'W': '|', 'w': ':', 'X': 'c', 'x': ';', 
             'Y': 'e', 'y': '}', 'Z': '"', 'z': 'f', ' ': ' ', '1':'e', '2':'G', '3':'c', '4':'h',
             '5':'i', '6':'j', '7':'d', '8':'k', '9':'q', '0':'g', '-':'J'}
    
    def encrypted_file():
        # Open and read the text file text.txt
        with open('text.txt', 'r') as text_file:
            file_contents = text_file.read()

        # Encrypt the text and write to encrypted.txt
        with open('encrypted.txt', 'w') as encrypted_file:
            for ch in file_contents:
                # If the character is in the dictionary, encrypt it
                encrypted_file.write(codes.get(ch, ch))

    def decrypted_file():
        # Decrypt the text of encrypted.txt
        with open('encrypted.txt', 'r') as encrypted_file:
            encrypted_contents = encrypted_file.read()

        # Reverse the dictionary for decryption 
        reverse_codes = {v: k for k, v in codes.items()}

        # Decrypt the text
        decrypted_text = ''
        for ch in encrypted_contents:
            decrypted_text += reverse_codes.get(ch, ch)
        return decrypted_text
    
    # Encrypt the content of text.txt and write to encrypted.txt
    encrypted_file()

    # Decrypt the content of encrypted.txt
    decrypted_text = decrypted_file()

    # Print the decrypted text to the console
    print("Decrypted text:\n")
    print(decrypted_text)

# Call the main function
if __name__ == "__main__":
    main()

