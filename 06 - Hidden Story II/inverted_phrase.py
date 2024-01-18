# EN
# Write a function that takes a string and returns each
# word of the string inverted and in lowercase letters, however
# with the words in the same order.
# Assume that the string does not have any accented letters,
# number or special character, letters and spaces only.

# PT
# Escreva uma função que recebe uma string e retorna cada
# Palavra da string invertida e em letras minúsculas, porém
# com as palavras na mesma ordem.
# Assuma que a string não possui nenhuma letra com acento,
# número ou caractere especial, apenas letras e espaços.

def inverted_phrase(phrase: str) -> str:
    """
    The function takes a phrase as input, splits it into words, and returns the inverted version of each
    word in lowercase, separated by spaces.
    
    :param phrase: The input phrase that you want to invert
    :type phrase: str
    :return: a string that represents the inverted version of the input phrase.
    """
    words = phrase.split(' ')
    inverted_word = ''
    for word in words:
        for i in range(len(word), 0, -1):
            inverted_word += word[i-1]
        if word != words[-1]:
            inverted_word += ' '
    return inverted_word.lower()