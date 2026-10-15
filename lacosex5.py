
import os
os.system("cls")



 
saldo = 500
 
while True:
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")
    opcao = input("Opção: ")
 
    match opcao:
        case "1":
            print(f"Saldo atual: R$ {saldo:.2f}")
        case "2":
            valor = float(input("Valor: R$ "))
            if valor > 0:
                saldo = saldo + valor
                print("Depósito realizado.")
            else:
                print("Valor inválido.")
        case "3":
            valor = float(input("Valor: R$ "))
            if valor <= 0:
                print("Valor inválido.")
            elif valor > saldo:
                print("Saldo insuficiente.")
            else:
                saldo = saldo - valor
                print("Saque realizado.")
        case "4":
            print(f"Saldo atual: R$ {saldo:.2f}")
            break
        case _:
            print("Opção inválida.")
 