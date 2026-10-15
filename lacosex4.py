import os
os.system("cls")

secreto = 68
tentativas = 0
 
while tentativas < 7:
    palpite = int(input("Palpite: "))
    tentativas = tentativas + 1
 
    if palpite == secreto:
        print(f"{palpite}: acertou em {tentativas} tentativas!")
        break
    elif palpite < secreto:
        print(f"{palpite}: tente um número maior.")
    else:
        print(f"{palpite}: tente um número menor.")
 
if palpite != secreto:
    print("Você perdeu! O número secreto era", secreto)
 