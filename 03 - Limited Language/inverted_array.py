# EN
# Write a function that takes an array and returns a new one
# array with all positions inverted from the original without
# change it. Do not use the methods of the global Array object.
# javascript (reverse, map, forEach, etc.).

# PT
# Escreva uma função que recebe um array e retorne um novo
# array com todas as posições invertidas do original sem
# altera-lo. Nao utilize os metodos do objeto global Array do
# javascript (reverse, map, forEach, etc).

def inverted_array(array: list) -> list:
    """
    The function takes an array as input and returns a new array with the elements in reverse order.
    
    :param array: The parameter `array` is a list of elements
    :type array: list
    :return: The function `inverted_array` returns a new list that is the inverted version of the input
    list.
    """
    inverted = []
    for i in range(len(array), 0, -1):
        inverted.append(array[i-1])
    return inverted
