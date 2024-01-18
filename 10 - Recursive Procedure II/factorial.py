# EN
# Write a function that takes a number and returns its
# factorial without using any repetition structure (while,
# dowhile, for, etc).
# The factorial of a number is equal to the multiplication of all
# positive integers less than or equal to it. She must be
# capable of returning correct integers even for
# high values.

# PT
# Escreva uma função que recebe um número e retorna o seu
# fatorial sem utilizar nenhuma estrutura de repetição (while,
# dowhile, for, etc).
# O fatorial de um número é igual a multiplicação de todos os
# inteiros positivos menores ou iguais a ele. Ela deve ser
# capaz de retornar números inteiros corretos mesmo para
# valores altos.

def factorial(num: int) -> int:
    """
    The factorial function calculates the factorial of a given number recursively.
    
    :param num: The parameter `num` is an integer that represents the number for which we want to
    calculate the factorial
    :type num: int
    :return: The factorial of the given number.
    """
    if num > 0:
        return num * factorial(num - 1)
    else:
        return 1