# EN
# Write a function that receives a string, checks if it
# has the same amount of each letter that makes it up and
# returns true if it has it or false if it doesn't have it.

# PT
# Escreva uma funçao que recebe uma string, verifica se ela
# possui a mesma quantidade de cada letra que a compõe e
# retorna true caso possua ou false caso não possua.


def is_amount_letter(string: str) -> bool:
    """
    The function checks if each letter in a string appears exactly once.
    
    :param string: The parameter `string` is a string that represents a word or phrase
    :type string: str
    :return: The function is_amount_letter is returning a boolean value.
    """
    string = list(string)
    for idx, element in enumerate(string):
        value = string.copy()
        value.pop(idx)
        if element in value:
            pass
        else:
            return False
    return True