idade = int(input("Idade: "))
tem_cnh = input("Tem cnh s/n? ")

if idade >= 18 and tem_cnh == "s":
    print("Pode dirigir!")
else:
    print("Não pode dirigir!")    