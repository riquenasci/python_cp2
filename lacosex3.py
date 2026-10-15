import os
os.system("cls")

soma = 0
quantidade = 0
 
nota = float(input("Nota (-1 para sair): "))
 
while nota != -1:
    if nota >= 0 and nota <= 10:
        soma = soma + nota
        quantidade = quantidade + 1
    else:
        print("Nota inválida.")
    nota = float(input("Nota (-1 para sair): "))
 
if quantidade == 0:
    print("Nenhuma nota válida foi digitada.")
else:
    media = soma / quantidade
    print("Quantidade de notas:", quantidade)
    print(f"Média da turma: {media:.2f}")
 
    if media < 5:
        print("Classificação: insuficiente")
    elif media < 7:
        print("Classificação: regular")
    elif media < 9:
        print("Classificação: boa")
    else:
        print("Classificação: excelente")