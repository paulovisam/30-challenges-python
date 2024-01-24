# EN
# Write a function that takes a string and a number
# and return the result of applying the Cesar Cipher to
# decrypt its contents, i.e., rewind each
# letter by the number passed in alphabetical order.

# PT
# Escreva uma funçao que recebe uma string e um numero
# e retorne o resultado da aplicação da Cifra de Cesar para
# descriptografar o seu conteúdo, ou seja, que retroceda cada
# letra pelo número passado seguindo a ordem alfabética.

def encript_cipher(string: str, number: int) -> int:
    cipher = ""
    for letter in string:
        if letter.isupper():
            letter = letter.lower()
            idx_letter = ord(letter) - ord("a")
            idx_letter = (idx_letter + number) % 26
            char = chr(idx_letter + ord("a")).upper()
            cipher += char
        else:
            idx_letter = ord(letter) - ord("a")
            idx_letter = (idx_letter + number) % 26
            char = chr(idx_letter + ord("a"))
            cipher += char
    return cipher

def decript_cipher(string: str, number: int) -> int:
    cipher = ""
    for letter in string:
        if letter.isupper():
            letter = letter.lower()
            idx_letter = ord(letter) - ord("a")
            idx_letter = (idx_letter - number) % 26
            char = chr(idx_letter + ord("a")).upper()
            cipher += char
        else:
            idx_letter = ord(letter) - ord("a")
            idx_letter = (idx_letter - number) % 26
            char = chr(idx_letter + ord("a"))
            cipher += char
    return cipher
