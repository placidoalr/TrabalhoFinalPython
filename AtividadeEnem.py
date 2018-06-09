import csv
listaTotal = open("C:\\GitHub\\TrabalhoFinalPython\\train.csv","r",encoding="utf-8")

lista = csv.reader(listaTotal,delimiter=",")
for contador in lista:
    print(contador)