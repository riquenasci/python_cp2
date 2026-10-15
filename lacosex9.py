import os
os.system("cls")
 
veiculos = 0
total = 0
 
placa = input("Placa (FIM para sair): ")
 
while placa != "FIM":
    horas = int(input("Horas: "))
 
    if horas <= 0:
        print("Quantidade de horas inválida.")
    else:
        valor = 8 + (horas - 1) * 5
        if horas > 8:
            valor = valor + 20
 
        print(f"{placa}: R$ {valor:.2f}")
        veiculos = veiculos + 1
        total = total + valor
 
    placa = input("Placa (FIM para sair): ")
 
print("Veículos atendidos:", veiculos)
print(f"Total arrecadado: R$ {total:.2f}")