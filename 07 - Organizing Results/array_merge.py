# EN
# Write a function that receives a two-dimensional array
# of integers and returns a single array containing all
# numbers in ascending order.

# PT
# Escreva uma funcao que recebe um array bidimensional
# de inteiros e retorna um único array contendo todos os
# números em ordem ascendente.


def array_merge(arrays: list) -> list:
    """
    The function takes a list of arrays, merges them into a single list, and returns the sorted result.
    
    :param arrays: The parameter "arrays" is a list of lists. Each inner list represents an array of
    elements
    :type arrays: list
    :return: The function `array_merge` returns a sorted list that contains all the elements from the
    input list of arrays.
    """
    result = []
    for array in arrays:
        for i in array:
            result.append(i)
    result.sort()
    return result