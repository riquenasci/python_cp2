import os
os.system("cls")
 
resposta = "S"
 
while resposta == "S":
    numero = int(input("Número: "))
    limite = int(input("Limite: "))
 
    if limite < 1 or limite > 20:
        print("Limite inválido! Digite um valor entre 1 e 20.")
    else:
        contador = 1
        while contador <= limite:
            print(f"{numero} x {contador} = {numero * contador}")
            i = i + 1
 
    resposta = input("Calcular outra? (S/N) ")
    while resposta != "S" and resposta != "N":
        print("Resposta inválida.")
        resposta = input("Calcular outra? (S/N) ")
 
print("Programa encerrado.")