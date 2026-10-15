
import os
os.system("cls")
 
positivos = 0
negativos = 0
pares = 0
impares = 0
soma = 0
quantidade = 0
maior = 0
menor = 0
 
numero = int(input("Número (0 para sair): "))
 
while numero != 0:
    quantidade = quantidade + 1
    soma = soma + numero
 
    if numero > 0:
        positivos = positivos + 1
    else:
        negativos = negativos + 1
 
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
 
    if quantidade == 1 or numero > maior:
        maior = numero
    if quantidade == 1 or numero < menor:
        menor = numero
 
    numero = int(input("Número (0 para sair): "))
 
if quantidade == 0:
    print("Nenhum número foi digitado.")
else:
    print("Positivos:", positivos)
    print("Negativos:", negativos)
    print("Pares:", pares)
    print("Ímpares:", impares)
    print("Soma:", soma)
    print("Maior:", maior)
    print("Menor:", menor)
 