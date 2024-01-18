# EN
# Write a function that takes a number and returns an equivalent quantity
# of "chunks" separated by a dash "-" without using any structure
# repetition (while, for, etc)

# PT
# Escreva uma função que recebe um número e retorna uma quantidade equivalente
# de "chunks" separados por um traço "-" sem utilizar nenhuma esatrutura de
# repetição (while, for, etc)



def chunk(n: int) -> str:
    """
    The function recursively generates a string that consists of "chunk-" repeated n times.
    
    :param n: The parameter `n` is an integer that represents the number of times the word "chunk"
    should be repeated
    :type n: int
    :return: a string that represents a sequence of "chunk" repeated n times.
    """
    var = ''
    if n != 1:
        var += "chunk-"+chunk(n-1)
    elif n == 1:
        var += "chunk"
    return var