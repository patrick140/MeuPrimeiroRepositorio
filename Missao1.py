#Adquirir os numeros inteiros
Numero1 = int(input("Digite o primeiro numero inteiro: "))
numero2 = int(input("Digite o segundo numero inteiro: "))
numero3 = int(input("Digite o terceiro numero inteiro: "))

#Primeiro bloco condicional para achar o menor numero
if Numero1 < numero2 and Numero1 < numero3:
    print("O menor numero é: ", Numero1)
else:
    if numero2 < Numero1 and numero2 < numero3:
        print("O menor numero é: ", numero2)
    else:
        if numero3 < Numero1 and numero3 < numero2:
            print("O menor numero é: ", numero3)

#Segundo bloco condicional para achar o numero do meio, fazendo o uso de ambas condicionais compostas "AND" e "OR"
if Numero1 > numero2 and Numero1 < numero3 or Numero1 < numero2 and Numero1 > numero3:
    print("O numero do meio é: ", Numero1)
else:
    if numero2 > Numero1 and numero2 < numero3 or numero2 < Numero1 and numero2 > numero3:
        print("O numero do meio é: ", numero2)
    else:
        if numero3 > Numero1 and numero3 < numero2 or numero3 < Numero1 and numero3 > numero2:
            print("O numero do meio é: ", numero3)

#Terceiro bloco condicional para achar o maior numero
if Numero1 > numero2 and Numero1 > numero3:
    print("O maior numero é: ", Numero1)
else:
    if numero2 > Numero1 and numero2 > numero3:
        print("O maior numero é: ", numero2)
    else:
        if numero3 > Numero1 and numero3 > numero2:
            print("O maior numero é: ", numero3)

