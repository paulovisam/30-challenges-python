# EN
# Write a function that takes any integer,
# square each of its digits and then
# concatenate the result returning a single integer.

# PT
# Escreva uma função que recebe um número inteiro qualquer,
# eleve ao quadrado cada um de seus algarismos e depois
# concatene o resultado retornando um único número inteiro.

def raise_to_square(number: int) -> int:
    """
    The function takes an integer as input, converts it to a string, squares each digit, concatenates
    the squared digits, and returns the result as an integer.
    
    :param number: An integer number that we want to raise to the square
    :type number: int
    :return: The function `raise_to_square` returns an integer value.
    """
    str_number = str(number)
    str_result = ''
    for i in range(len(str_number)):
        str_result += str(int(str_number[i])**2)
    return int(str_result)