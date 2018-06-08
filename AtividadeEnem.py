import csv
listaTotal = open("C:\\GitHub\\TrabalhoFinalPython\\train.csv","r")
lista = csv.reader(listaTotal,delimiter=",")
for contador in lista:
    print(contador)