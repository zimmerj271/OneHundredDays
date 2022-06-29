alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = [' ','!','@','#','$','%','^','&','*','(',')','-','+','=','_','[',']','{','}','|','\\',';',"'",'"','<','>',',','.','/','?','1','2','3','4','5','6','7','8','9','0']


def encrypt(text, shift):
    cipher_text_array = []
    for char in text:
        if char in symbols:
            new_char = char
            continue
        idx = alphabet.index(char)
        if idx + shift > len(alphabet) - 1:
            shifted_index = shift - (len(alphabet) - idx)
            new_char = alphabet[shifted_index]
            
        else:
            new_char = alphabet[idx + shift]

        cipher_text_array.append(new_char)
        cipher_text = ''.join(cipher_text_array)
    return cipher_text


def decrypt(text, shift):
    decipher_text_array = []
    for char in text:
        if char in symbols:
            new_char = char
            continue
        idx = alphabet.index(char)
        if idx - shift < 0:
            shifted_index = len(alphabet) - (shift - idx) 
            new_char = alphabet[shifted_index]
        else:
            new_char = alphabet[idx - shift]

        decipher_text_array.append(new_char)
        decipher_text = ''.join(decipher_text_array)
    return decipher_text

def caesar(choice, text, shift):
    cipher_text_array = []
    for char in text:
        if char in symbols:
            new_char = char
            cipher_text_array.append(new_char)
            continue
        
        idx = alphabet.index(char)
        if choice == 'encode':
            if idx + shift > len(alphabet) - 1:
                shifted_index = shift - (len(alphabet) - idx)
                new_char = alphabet[shifted_index]
            else:
                new_char = alphabet[idx + shift]
        else:
            if idx - shift < 0:
                shifted_index = len(alphabet) - (shift - idx) 
                new_char = alphabet[shifted_index]  
            else:
                new_char = alphabet[idx - shift]

        cipher_text_array.append(new_char)
    cipher_text = ''.join(cipher_text_array)
    print(cipher_text)


working = True
while working:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    go_again = input("Would you like to go again? [yes/no]: ").lower()
    if go_again == 'no':
        working = False