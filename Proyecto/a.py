def conjunto_pnto(M, s):
    lista_ptos = []
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == s:
                lista_ptos.append([i,j])
    return lista_ptos
def verificar(M, lista_ptos, s):
    si = True
    for punto in lista_ptos:
        if si == False:
            return False
        else:
            si = (si and (M[punto[0]][punto[1]] == s))
    return si
def iniciar():
    print("¡¡ BIENVENIDO A EZ_BINGO!!")
    print("paso 1: Ingresa tus bingos ")
    print("Por ejemplo:")
    print("1  21 39 59 62")
    print("2  22 35 52 67")
    print("10 19 44 48 70")
    print("8  16 40 60 73")
    print("11 18 45 55 61")
    print("paso 2: Pon '"'no'"' para terminar de ingresar tus bingos y luego sigue las instrucciones ")
    print("paso 3: Dibuja la forma de juego con X\'s y O\'s (no olvides que los X\'s definen la forma)")
    print("Por ejemplo:")
    print("X X X X X")
    print("X 0 0 0 X")
    print("X 0 0 0 X")
    print("X 0 0 0 X")
    print("X X X X X")
    print("!! Comenzemos !!")
def imprimirbin(bingo):
    for fila in bingo :
        for elemento in fila:
            if len(elemento) == 1:
                print(elemento,end="  ")
            elif len(elemento)==2:
                print(elemento,end=" ")
        print()
