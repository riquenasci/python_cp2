import os
os.system("cls")

while True:
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")
    opcao = input("Opção: ")
 
    match opcao:
        case "1":
            n1 = float(input("Primeiro número: "))
            n2 = float(input("Segundo número: "))
            print("Resultado:", n1 + n2)
        case "2":
            n1 = float(input("Primeiro número: "))
            n2 = float(input("Segundo número: "))
            print("Resultado:", n1 - n2)
        case "3":
            n1 = float(input("Primeiro número: "))
            n2 = float(input("Segundo número: "))
            print("Resultado:", n1 * n2)
        case "4":
            n1 = float(input("Primeiro número: "))
            n2 = float(input("Segundo número: "))
            if n2 == 0:
                print("Não é possível dividir por zero.")
            else:
                print("Resultado:", n1 / n2)
        case "5":
            print("Fim do programa.")
            break
        case _:
            print("Opção inválida.")