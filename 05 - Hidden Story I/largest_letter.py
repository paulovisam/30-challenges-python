# EN
# Write a function that takes a string and returns the
# largest letter in lowercase alphabetical order.
# Assume that the string does not have any letters with
# accent, number or special character, letters only
# and spaces.

# PT
# Escreva uma função que recebe uma string e retorna a
# maior letra segundo a ordem alfabética em minúsculo.
# Assuma que a string não possui nenhuma letra com
# acento, número ou caractere especial, apenas letras
# e espaços.


def largest_letter(string: str) -> str:
    """
    The function "largest_letter" takes a string as input and returns the largest letter in the string,
    converted to lowercase.
    
    :param string: A string that represents a sequence of characters
    :type string: str
    :return: the largest letter in the given string, converted to lowercase.
    """
    return sorted(string)[-1].lower()