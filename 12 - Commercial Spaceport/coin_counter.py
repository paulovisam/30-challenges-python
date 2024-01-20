# EN
# Write a function that takes an integer value and returns
# the quantity of each coin to arrive at the value.
# There are coins of 1, 5, 10, 25, 100, 500.
# You should always prioritize the highest value coins.
# (as many 500 coins as possible, then as many
# possible 100 coins, etc.).

# PT
# Escreva uma funçao que receba um valor inteiro e retorne
# a quantidade de cada moeda para se chegar ao valor.
# Existem moedas de 1, 5, 10, 25, 100, 500.
# Deve-se sempre priorizar as moedas de maior valor.
# (o máximo possível de moedas de 500, depois o máximo
# possível de moedas de 100, etc).

def coin_counter(value: int) -> dict:
    """
    The function `coin_counter` takes an integer value as input and returns a dictionary containing the
    number of coins needed to make up that value using denominations of 500, 100, 25, 10, 5, and 1.
    
    :param value: The value parameter represents the amount of money that needs to be counted in terms
    of coins
    :type value: int
    :return: a dictionary that represents the amount of each coin needed to make up the given value.
    """
    coins = [500,100,25,10,5,1]
    amount_coin = {}
    for coin in coins:
        div = value/coin
        if div >= 1:
            amount_coin[str(coin)] = value//coin
            if div == 1:
                value = 0
                continue
            rest = value%coin
            if rest > 0:
                value = rest
        else:
            amount_coin[str(coin)] = 0
            continue
    return amount_coin

