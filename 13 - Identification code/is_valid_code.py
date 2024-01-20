# EN
# Write a function that takes a number and checks whether it
# is a valid identification code according to the rules of
# creation of the check digit. The creation of the check digit
# it works as follows:
# 1. Add the digits in even positions (odd if
# counting from 1)
# 2. Multiply this result by 3
# 3. Add the digits in the odd positions (even if
# counting from 1) of the original number and then add that
# result to the result of the previous step
# 4. Find the remainder after dividing the result from the previous step
# for 10
# 5. If the remainder of the division is 0, the check digit is 0, so
# otherwise the check digit is 10 - remainder

# PT
# Escreva uma função que recebe um número e verifica se ele
# é um código de identificação válido segundo as regras de
# criação do dígito verificador. O código é composto por 12
# algarismos sendo o ultimo o digito verificador.
# A criação do dígito verificador funciona da seguinte forma:
# 1. Some os dígitos das posições pares (ímpares se estiver
# contando a partir de 1)
# 2. Multiplique esse resultado por 3
# 3. Some os dígitos das posições ímpares (pares se estiver
# contando a partir de 1) do número original e então some esse
# resultado ao resultado do passo anterior
# 4. Encontre o resto da divisão do resultado do passo anterior
# por 10
# 5. Se o resto da divisão for 0, o dígito verificador é 0, do
# contrário o dígito verificador é 10 - resto


def is_valid_code(code: int) -> bool:
    """
    The function `is_valid_code` checks if a given code is valid by calculating a verifying digit based
    on the code and comparing it to the last digit of the code.
    
    :param code: The code parameter is an integer that represents a code
    :type code: int
    :return: a boolean value indicating whether the given code is valid or not.
    """
    pairs, odd = 0,0
    #Trasforms in array string
    code = str(code)
    # Remove digit
    verifying_digit = int(code[-1])
    code = code[0:-1]
    for idx, value in enumerate(code):
        if idx%2 == 0:
            #Get pairs numbers
            pairs += int(value)
        else:
            #Get odd numbers
            odd += int(value)
    total = (pairs* 3)+odd
    rest = total%10
    if rest == 0:
        return verifying_digit==0
    else:
        return verifying_digit==(10-rest)
