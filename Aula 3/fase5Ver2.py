Tem_ingresso = input("Você tem ingresso? (sim ou não)")

aniversariante = input("Você é anniversariante? (sim ou não)")

if Tem_ingresso == "sim": 
    Tem_ingresso = True
else:
    Tem_ingresso = False

if aniversariante == "sim":
    aniversariante = True
else:
    aniversariante = False

if Tem_ingresso == True or aniversariante == True:
    print("Entrada Liberada!")
else:
    print("Você precisa comprar um ingresso")

