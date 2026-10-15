import os
os.system("cls")


senha_correta = "1234"
tentativas = 0
 
while tentativas < 3:
    senha = input("Senha: ")
    tentativas = tentativas + 1
 
    if senha == senha_correta:
        print("Acesso permitido.")
        break
    else:
        print("Senha incorreta. Tentativas restantes:", 3 - tentativas)
 
if senha != senha_correta:
    print("Acesso bloqueado.")
 