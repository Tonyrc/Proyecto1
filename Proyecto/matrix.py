from a import *
iniciar()
lista_matrix = []
lista_matrix2 = []
M = []
N = []
a="si"
while True:
    if (len(M) == 0 and a == "si"):
        print("B I N G O Nº"+ str(len(lista_matrix)+1)+":")
    n = input()
    if n != "ready":
        if len(M) < 5:
            M.append(n.split())
            N.append(n.split())
        if len(M) == 5:
            lista_matrix.append(M)
            lista_matrix2.append(N)
            M = []
            N = []
            print("¿Quieres ingresar un bingo más? si/no")
            a = input()
            if a =="no":
                print("entonces escribe ready ")

    else:
        break
M = []
N = []
print("Coloca la forma del bingo ganador: ")
for i in range(5):
    M.append(input().split())
lista_puntos = conjunto_pnto(M, "X")
#minimo_jugadas = len(lista_puntos)

while not any(verificar(lista_matrix[i], lista_puntos, "X") for i in range(len(lista_matrix))):
    print("Ingresa el número del bingo: ")
    numero = input()
    for k, matriz in enumerate(lista_matrix):
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == numero:
                    matriz[i][j] = "X"
        print()
        print("B I N G O N°", k+1)

        imprimirbin(matriz)
n = 0
for i in range(len(lista_matrix)):
    if verificar(lista_matrix[i], lista_puntos, "X") :
        n+=1
if n ==1:
    print()
    print("Tu bingo ganador es: ")
    print()
if n >1:
    print()
    print("Tus bingos ganadores son: ")
    print()

for matriz in lista_matrix:
    if verificar(matriz, lista_puntos, "X"):
        indice = lista_matrix.index(matriz)
        ganador = lista_matrix2[indice]

        print("B I N G O N°",indice+1)
        imprimirbin(ganador)
