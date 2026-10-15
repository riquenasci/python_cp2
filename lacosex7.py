import os
os.system("cls")
 
eleitores = int(input("Eleitores: "))
 
projeto1 = 0
projeto2 = 0
projeto3 = 0
brancos = 0
nulos = 0
 
contador = 1
while contador <= eleitores:
    voto = input("Voto (1, 2, 3 ou 0 para branco): ")
 
    match voto:
        case "1":
            projeto1 = projeto1 + 1
        case "2":
            projeto2 = projeto2 + 1
        case "3":
            projeto3 = projeto3 + 1
        case "0":
            brancos = brancos + 1
        case _:
            nulos = nulos + 1
 
    contador = contador + 1
 
print("Projeto 1:", projeto1)
print("Projeto 2:", projeto2)
print("Projeto 3:", projeto3)
print("Brancos:", brancos)
print("Nulos:", nulos)
 
if projeto1 > projeto2 and projeto1 > projeto3:
    print("Vencedor: projeto 1")
elif projeto2 > projeto1 and projeto2 > projeto3:
    print("Vencedor: projeto 2")
elif projeto3 > projeto1 and projeto3 > projeto2:
    print("Vencedor: projeto 3")
else:
    print("Empate.")