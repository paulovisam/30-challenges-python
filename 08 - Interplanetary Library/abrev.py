# EN
# Write a function that receives a string containing a
# full name and returns a string with all names,
# except the last, abbreviated and the last name in letters
# Capital letters before abbreviations separated by commas.

# PT
# Escreva uma funçao que recebe uma string contendo um
# nome completo e retorna uma string com todos os nomes,
# exceto o último, abreviados e o último nome em letras
# maiúsculas antes das abreviações separado por vírgula.

def abrev(name: str) -> str:
    """
    The function `abrev` takes a name as input and returns the abbreviated form of the name, where the
    last name is followed by a comma and the first names are represented by their first initials
    followed by a period.
    
    :param name: The parameter `name` is a string that represents a person's full name
    :type name: str
    :return: a string that represents the abbreviated form of a given name.
    """
    name = name.upper()
    array_name = name.split(' ')
    name_abv = array_name[-1]+','
    for i in range(len(array_name)-1):
        name_abv += ' '+array_name[i][0]+'.'
    print(name_abv)
    return name_abv
