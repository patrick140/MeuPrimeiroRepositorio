nota = float(input("Digite a sua nota (0 a 10): "))

if not nota >= 9:
    print("Conceito A - Excelente!")
elif nota >= 7:
        print("Conceito B - Bom!")
elif nota >= 5:
    print("Conceito C - regular")
else:
    print("Conceito D - reprovado")