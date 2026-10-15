import os
os.system("cls")
 
produto = input("Produto: ")
preco = float(input("Preço: R$ "))
estoque = int(input("Estoque inicial: "))
total_vendido = 0
 
while True:
    print("1 - Consultar estoque")
    print("2 - Repor")
    print("3 - Vender")
    print("4 - Sair")
    opcao = input("Opção: ")
 
    match opcao:
        case "1":
            print(f"{produto}: {estoque} unidades")
        case "2":
            quantidade = int(input("Reposição: "))
            if quantidade > 0:
                estoque = estoque + quantidade
                print("Reposição realizada.")
            else:
                print("Quantidade inválida.")
        case "3":
            quantidade = int(input("Venda: "))
            if quantidade <= 0:
                print("Quantidade inválida.")
            elif quantidade > estoque:
                print("Estoque insuficiente.")
            else:
                estoque = estoque - quantidade
                total_vendido = total_vendido + quantidade * preco
                print("Venda realizada.")
        case "4":
            print("Estoque restante:", estoque, "unidades")
            print(f"Valor total vendido: R$ {total_vendido:.2f}")
            break
        case _:
            print("Opção inválida.")