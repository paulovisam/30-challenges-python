# EN
# Write a function that takes an ordered pair (x, y) and
# return an array of (x, y) pairs where each of them has
# x and y less than or equal to the pair received in ascending order.
# The pairs must be ordered so that first
# increase the value of y and then the value of x.
# Only the quadrant where x and y are positive should be
# considered.

# PT
# Escreva uma função que receba um par ordenado (x, y) e
# retorne um array de pares (x, y) onde cada um deles possui
# x e y menor ou igual ao par recebido em ordem crescente.
# Os pares devem ser ordenados de forma que primeiro
# aumente o valor de y e depois o valor de x.
# Apenas o quadrante onde x e y são positivos deve ser
# considerado.

def ordered_pairs(ordered: list):
    """
    The function "ordered_pairs" takes in a list of two ordered numbers and returns a list of all
    possible ordered pairs of non-negative integers up to the given numbers.
    
    :param ordered: The parameter "ordered" is a list that contains two elements
    :type ordered: list
    :return: a list of ordered pairs.
    """
    pairs = []
    if ordered[0] >= 0 and ordered[1] >= 0:
        for x in range(0, ordered[0]+1):
            for y in range(0, ordered[1]+1):
                pairs.append([x, y])
    return pairs