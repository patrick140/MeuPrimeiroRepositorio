nota = float(input("Digite a sua nota (0 a 10): "))

if nota >= 9:
    print("Conceito A - Excelente!")
else:
    if nota >= 7:
        print("Conceito B - Bom!")
    else:
        if nota >= 5:
            print("Conceito C - regular")
        else:
            print("Conceito D - reprovado")