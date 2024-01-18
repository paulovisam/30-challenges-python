# EN
# Write a function that takes any number
# of integers as arguments and return the average
# arithmetic between them

# PT
# Escreva uma função que recebe um número qualquer
# de números inteiros como argumentos e retorne a média
# aritmética entre eles

def arithmetic_average(values: list) -> float:
    """
    The function calculates the arithmetic average of a list of values.
    
    :param values: A list of numerical values for which you want to calculate the arithmetic average
    :type values: list
    :return: The arithmetic average of the values in the list.
    """
    total = 0
    for value in values:
        total += value
    return total/len(values)