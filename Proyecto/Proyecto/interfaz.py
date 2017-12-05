from tkinter import *

def imprimirbin(bingo):
   for fila in bingo :
       for elemento in fila:
           if len(elemento) == 1:
               print(elemento,end="  ")
           elif len(elemento)==2:
               print(elemento,end=" ")
       print()
def verificar(M, lista_ptos, s):
 si = True
 for punto in lista_ptos:
     if si == False:
         return False
     else:
         si = (si and (M[punto[0]][punto[1]] == s))
 return si
def conjunto_pnto(M, s):
 lista_ptos = []
 for i in range(len(M)):
     for j in range(len(M[i])):
         if M[i][j] == s:
             lista_ptos.append([i,j])
 return lista_ptos
def obtener_bingo():
  numeros = [[B1.get(),I1.get(),N1.get() ,G1.get(),O1.get(),],
              [B2.get(),I2.get(),N2.get(),G2.get(),O2.get()],
              [B3.get(),I3.get(),"O"     ,G3.get(),O3.get()],
               [B4.get(),I4.get(),N4.get(),G4.get(),O4.get()],
                [B5.get(),I5.get(),N5.get(),G5.get(),O5.get()]]
  return numeros

def unomas():


   numero_bingo = numero.get()
   numero_bingo = numero_bingo[8::]
   bingo = obtener_bingo()
   lista_matrix[numero_bingo] = bingo
   lista_matrix2[numero_bingo] = bingo
   bin = len(lista_matrix)
   lista_matrix["bingo N°"+str(bin+1)]= [["", "", "", "", ""],
                                         ["", "", "", "", ""],
                                         ["", "", "o", "", ""],
                                         ["", "", "", "", ""],
                                         ["", "", "", "", ""]]
   lista_matrix2["bingo N°" + str(bin + 1)] = [["", "", "", "", ""],
                                              ["", "", "", "", ""],
                                              ["", "", "o", "", ""],
                                              ["", "", "", "", ""],
                                              ["", "", "", "", ""]]


   opciones.append("bingo N°"+str(bin+1))
   show = OptionMenu(ventana, var, *opciones).place(x=340, y=20)
   limpiar()
   return numero.set("Ingresa bingo N°"+str(bin+1))
def limpiar():
   B1.set("")
   B2.set("")
   B3.set("")
   B4.set("")
   B5.set("")
   I1.set("")
   I2.set("")
   I3.set("")
   I4.set("")
   I5.set("")
   N1.set("")
   N2.set("")
   N4.set("")
   N5.set("")
   G1.set("")
   G2.set("")
   G3.set("")
   G4.set("")
   G5.set("")
   O1.set("")
   O2.set("")
   O3.set("")
   O4.set("")
   O5.set("")

def guardar():
   bingo = obtener_bingo()
   numero_bingo = numero.get()
   numero_bingo = numero_bingo[8::]

   lista_matrix[numero_bingo]=bingo
   lista_matrix2[numero_bingo]=bingo
   if numero_bingo not in opciones:
       opciones.append(numero_bingo)
   show = OptionMenu(ventana, var, *opciones).place(x=340, y=20)

def imprimir():
   print(lista_matrix)
   print(lista_matrix2)
   print(opciones)
   print(var.get())
   print(lista_matrix["forma de juego"])
   print(a)

def mostrar_bingo():
   bingo = var.get()
   matris = lista_matrix[bingo]
   numero.set(bingo)
   B1.set(matris[0][0])
   B2.set(matris[1][0])
   B3.set(matris[2][0])
   B4.set(matris[3][0])
   B5.set(matris[4][0])
   I1.set(matris[0][1])
   I2.set(matris[1][1])
   I3.set(matris[2][1])
   I4.set(matris[3][1])
   I5.set(matris[4][1])
   N1.set(matris[0][2])
   N2.set(matris[1][2])
   N4.set(matris[3][2])
   N5.set(matris[4][2])
   G1.set(matris[0][3])
   G2.set(matris[1][3])
   G3.set(matris[2][3])
   G4.set(matris[3][3])
   G5.set(matris[4][3])
   O1.set(matris[0][4])
   O2.set(matris[1][4])
   O3.set(matris[2][4])
   O4.set(matris[3][4])
   O5.set(matris[4][4])
def ingresar_forma():
   limpiar()
   return numero.set("Ingresa forma de juego")

def empezar():
   def ingresar_numero():
       a.append(bolas.get())
       verificar_bingo()
       verificar_bingo()
       return bolas.set("")
   forma = lista_matrix2.pop("forma de juego")
   lista_bingos = generar_lista(lista_matrix2)
   lista_bingos2 = [i for i in lista_bingos]
   lista_puntos = conjunto_pnto(forma, "X")
   ing = Label(ventana,text="Ingresa los numero aqui",fg="white", bg="gray29",font=(40)).place(x =300,y=270)
   Marcar = Button(ventana,text ="<>",command=ingresar_numero).place(x=380,y=305)
   bolas.set("")
   bol = Entry(ventana,textvariable=bolas, width=2,font=("w",20)).place(x=340,y=300)
   def verificar_bingo():
     if not any(verificar(lista_bingos[i], lista_puntos, "X") for i in range(len(lista_bingos))):
         for bingo in lista_bingos:
             for i in range(len(bingo)):
                 for j in range(len(bingo[i])):
                     if bingo[i][j] == a[-1]:
                         bingo[i][j] = "X"
             imprimirbin(bingo)
     else:
         ganaste = Tk()
         ganaste.title("Ganaste")
         ganaste.configure(bg='gray29')
         G = Label(ganaste, text="¡TIENES UN BINGO GANADOR \n FELICIDADES!",fg="white",bg='gray29',font=("w",30)).pack()
         ganadores = []
         for k, matriz in enumerate (lista_bingos):
             if verificar(matriz, lista_puntos, "X"):
                 indice = lista_bingos.index(matriz)
                 ganador = lista_bingos2[indice]
                 ganadores.append(k)

                 print("ganador")
                 print(indice)
                 imprimirbin(ganador)
         ganadores = [str(int(i)+1) for i in ganadores]
         h = ""
         print(ganadores)
         for i in ganadores:
             h = h+"Bingo N°"+i+"\n"
         _Bin_g = Label(ganaste,text=h,fg="white",bg='gray29',font=("w",20)).pack()

def generar_lista(diccionario):
  lista = []
  for i in diccionario.values():
      lista.append(i)
  return lista

def option_changed(*opciones):
   bingo = var.get()
   print(bingo)
   matris = lista_matrix[bingo]
   B1.set(matris[0][0])
   B2.set(matris[1][0])
   B3.set(matris[2][0])
   B5.set(matris[4][0])
   I1.set(matris[0][1])
   I2.set(matris[1][1])
   I3.set(matris[2][1])
   I4.set(matris[3][1])
   I5.set(matris[4][1])
   N1.set(matris[0][2])
   N2.set(matris[1][2])
   N4.set(matris[3][2])
   N5.set(matris[4][2])
   G1.set(matris[0][3])
   G2.set(matris[1][3])
   G3.set(matris[2][3])
   G4.set(matris[3][3])
   G5.set(matris[4][3])
   O1.set(matris[0][4])
   O2.set(matris[1][4])
   O3.set(matris[2][4])
   O4.set(matris[3][4])
   O5.set(matris[4][4])
   return numero.set("Ingresa "+bingo)


ventana = Tk()
ventana.title("Easy_Bingo")
ventana.geometry("470x500")
ventana.configure(background='gray29')
Ver =Label(ventana,text="ver",bg="gray29",fg="white",font=("ver",15)).place(x=275,y=20)
separador=Label(ventana, text="\n"*32, bg="black").place(x=250,y=0)
numero = StringVar()
numero.set("Ingresa bingo N°1")
etiqueta1 = Label(ventana, textvariable=numero,fg="white", bg="gray29",font=(40)).place(x=5, y=20)

a = []

bolas = StringVar()

#gray29
#imputs
#SpringGreen3

bingoetiqueta= Label(ventana, text="                   \n\n\n\n\n", bg='Green3',fg="white", font=("B I N G O", 30)).place(x=10, y=80)
etiquetaB = Label(ventana, text="B", bg='Green3',fg="white", font=("B", 30)).place(x=10, y=80)
etiquetaI = Label(ventana, text="I", bg='Green3',fg="white", font=("I", 30)).place(x=54, y=80)
etiquetaN = Label(ventana, text="N", bg='Green3',fg="white", font=("N", 30)).place(x=93, y=80)
etiquetaG = Label(ventana, text="G", bg='Green3',fg="white", font=("G", 30)).place(x=137, y=80)
etiquetaO = Label(ventana, text="O", bg='Green3',fg="white", font=("O", 30)).place(x=180, y=80)
#Bingo
B1 = StringVar()
B1caja = Entry(ventana, textvariable=B1, width=2,font=("w",20)).place(x=17, y=140)
B2 = StringVar()
B2caja = Entry(ventana, textvariable=B2, width=2,font=("w",20)).place(x=17, y=180)
B3 = StringVar()
B3caja = Entry(ventana, textvariable=B3, width=2,font=("w",20)).place(x=17, y=220)
B4 = StringVar()
B4caja = Entry(ventana, textvariable=B4, width=2,font=("w",20)).place(x=17, y=260)
B5 = StringVar()
B5caja = Entry(ventana, textvariable=B5, width=2,font=("w",20)).place(x=17, y=300)
I1 = StringVar()
I1caja = Entry(ventana, textvariable=I1, width=2,font=("w",20)).place(x=57, y=140)
I2 = StringVar()
I2caja = Entry(ventana, textvariable=I2, width=2,font=("w",20)).place(x=57, y=180)
I3 = StringVar()
I3caja = Entry(ventana, textvariable=I3, width=2,font=("w",20)).place(x=57, y=220)
I4 = StringVar()
I4caja = Entry(ventana, textvariable=I4, width=2,font=("w",20)).place(x=57, y=260)
I5 = StringVar()
I5caja = Entry(ventana, textvariable=I5, width=2,font=("w",20)).place(x=57, y=300)
N1 = StringVar()
N1caja = Entry(ventana, textvariable=N1, width=2,font=("w",20)).place(x=97, y=140)
N2 = StringVar()
N2caja = Entry(ventana, textvariable=N2, width=2,font=("w",20)).place(x=97, y=180)
medio = Label(ventana,text="Free\nSpace",width=4).place(x=97, y=220)
N4 = StringVar()
N4caja = Entry(ventana, textvariable=N4, width=2,font=("w",20)).place(x=97, y=260)
N5 = StringVar()
N5caja = Entry(ventana, textvariable=N5, width=2,font=("w",20)).place(x=97, y=300)
G1 = StringVar()
G1caja = Entry(ventana, textvariable=G1, width=2,font=("w",20)).place(x=137, y=140)
G2 = StringVar()
G2caja = Entry(ventana, textvariable=G2, width=2,font=("w",20)).place(x=137, y=180)
G3 = StringVar()
G3caja = Entry(ventana, textvariable=G3, width=2,font=("w",20)).place(x=137, y=220)
G4 = StringVar()
G4caja = Entry(ventana, textvariable=G4, width=2,font=("w",20)).place(x=137, y=260)
G5 = StringVar()
G5caja = Entry(ventana, textvariable=G5, width=2,font=("w",20)).place(x=137, y=300)
O1 = StringVar()
O1caja = Entry(ventana, textvariable=O1, width=2,font=("w",20)).place(x=177, y=140)
O2 = StringVar()
O2caja = Entry(ventana, textvariable=O2, width=2,font=("w",20)).place(x=177, y=180)
O3 = StringVar()
O3caja = Entry(ventana, textvariable=O3, width=2,font=("w",20)).place(x=177, y=220)
O4 = StringVar()
O4caja = Entry(ventana, textvariable=O4, width=2,font=("w",20)).place(x=177, y=260)
O5 = StringVar()
O5caja = Entry(ventana, textvariable=O5, width=2,font=("w",20)).place(x=177, y=300)

lista_matrix = {"bingo N°1":[["","","","",""],
                         ["","","","",""],
                         ["","","o","",""],
                         ["","","","",""],
                         ["","","","",""]]}

lista_matrix2 = {"bingo N°1":[["","","","",""],
                         ["","","","",""],
                         ["","","o","",""],
                         ["","","","",""],
                         ["","","","",""]]}

var =StringVar(ventana)
var.set("bingo N°1")
var.trace("w", option_changed)

opciones =["bingo N°1"]
show = OptionMenu(ventana, var, *opciones).place(x=340, y=20)
#Botones
Unbingomas = Button(ventana, text="+", command=unomas,font=("w",16), bg="SpringGreen3",fg="black",borderwidth=4).place(x=210,y=10)
empezar = Button(ventana, text="Empezar",command=empezar,font=(40)).place(x=320,y=400)
guardar = Button(ventana, text="Guardar",bg="SpringGreen3",command=guardar ,fg="black").place(x=30,y=400)
Limpiar = Button(ventana, text="Limpiar",command=limpiar,fg="black",bg="SpringGreen3").place(x=140,y=400)
#imprimir = Button(ventana, text="Imprimir",command=imprimir).place(x=80, y=400)
Ingresar_forma = Button(ventana, text="Ingresa forma",command=ingresar_forma,fg="black",bg="SpringGreen3" ).place(x=10, y=50)
ventana.mainloop()
