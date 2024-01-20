# EN
# Write a class that contains a method to generate
# a flight license and the following attributes:
# . Name
# . Surname
# · Date of birth
# · Flight License (which must always start as false)
# 
# Furthermore, the class must have a method to create a
# license if the person does not already have one. The license
# must be a string following the following pattern:
# 
# · The first five characters of the surname in letters
# capital letters (completed with 9's if there are less than
# five)
# · The 6th character is a dash (-)
# · The 7th character is the digit of the decade (penultimate) of the
# year of birth
# · The 8th and 9th characters are the month of birth
# · The 10th character is the digit of the year (last) of the year
# of birth
# · The 11th character is a period (.)
# · The 12th character is the first letter of the first name
# (lower case)

# PT
# Escreva uma classe que contenha um método para gerar
# uma licença de voo e os seguintes atributos:
# . Nome
# . Sobrenome
# · Data de Nascimento
# · Licença de Voo (que deve iniciar sempre como falso)
# 
# Além disso a classe deve possuir um método para criar uma
# licença caso a pessoa ainda não possua uma. A licença
# deve ser uma string seguindo o seguinte padrão:
# 
# · Os primeiros cinco caracteres do sobrenome em letras
# maiúsculas (completado com 9 caso possua menos de
# cinco)
# · O 6° caractere é um traço (-)
# · O 7° caractere é o algarismo da década (penúltimo) do
# ano de nascimento
# · O 8° e 9° caracteres são o mês de nascimento
# · O 10° caractere é o algarismo do ano (último) do ano
# de nascimento
# · O 11° caractere é um ponto (.)
# · O 12° caractere é a primeira letra do primeiro nome
# (minúscula)

from datetime import datetime
class FlightLicense():
    def __init__(self, fist_name, last_name, birth: datetime, license: bool = False) -> None:
        """
        The FlightLicense class creates a flight license with a unique code based on the user's name and birthdate.
        """
        self.fist_name = fist_name
        self.last_name = last_name
        self.birth = birth
        self.license = license

    def create(self) -> str:
        """
        The function creates a new license based on the person's last name, birth year, birth month, and
        first name.
        :return: a string, which is the newly created license.
        """
        if not self.license:
            new_license = self.last_name[0:5].upper()
            for i in range(len(new_license)):
                if len(new_license) < 5:
                    new_license+='9'
            new_license+='-'
            new_license+=str(self.birth.year)[-2]
            new_license+=self.birth.strftime('%m')
            new_license+=str(self.birth.year)[-1]
            new_license+='.'
            new_license+=self.fist_name[0].lower()
            return new_license