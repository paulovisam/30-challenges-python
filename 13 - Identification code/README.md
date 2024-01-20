# 13 - Identification code

Write a function that takes a number and checks whether it
is a valid identification code according to the rules of
creation of the check digit. The creation of the check digit
it works as follows:
1. Add the digits in even positions (odd if
counting from 1)
2. Multiply this result by 3
3. Add the digits in the odd positions (even if
counting from 1) of the original number and then add that
result to the result of the previous step
4. Find the remainder after dividing the result from the previous step
for 10
5. If the remainder of the division is 0, the check digit is 0, so
otherwise the check digit is 10 - remainder

---

Escreva uma função que recebe um número e verifica se ele
é um código de identificação válido segundo as regras de
criação do dígito verificador. O código é composto por 12
algarismos sendo o ultimo o digito verificador.
A criação do dígito verificador funciona da seguinte forma:
1. Some os dígitos das posições pares (ímpares se estiver
contando a partir de 1)
2. Multiplique esse resultado por 3
3. Some os dígitos das posições ímpares (pares se estiver
contando a partir de 1) do número original e então some esse
resultado ao resultado do passo anterior
4. Encontre o resto da divisão do resultado do passo anterior
por 10
5. Se o resto da divisão for 0, o dígito verificador é 0, do
contrário o dígito verificador é 10 - resto