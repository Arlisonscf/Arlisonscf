#Aula de lista
from typing import List


lista = [2,8,10,12,14,16,'coxinha','maionese','molho','biscoito']
print(type(lista))
print("primeiro item da lista:",lista[0])
print("Último item da lista:",lista[9])
print("Último item da lista:",lista[-1])
print("Penútimo item da lista:",lista[-2])
print("Quantidade de itens da lista:",len(lista))
pc=["Mouse","Monitor","HD","Memória Ram","Câmera","Fone","HUB"]

#Mostra a lista em ordem alfabetica e dá prioridade a Letras maiusculas
print(sorted(pc))
List2 = [6,8,4,11,10,12,13]
print(sorted(List2))

#mostrar intervalos da lista 
print(List2)
print(List2[2:5])
print(List2[3:])
print(List2[:4])
List2.append(100)
print(List2)

#inserir item em posição determinada da lista 
List2.insert(2,500)
print(List2)

#unir duas listas
List2.extend(lista)
print(List2)

#remover último item da lista ou a indice infomado 
List2.pop(5)
print(List2)

#remover itrm especifico da lista 
List2.remove('10')
print(List2)
#copiar refriencia
lista3 = pc
#copiar objeto 
lista4 = pc.copy()
print("lista3",lista3)
print("lisrta4", lista4)

pc.append("SSD")
pc.append("Teclado")
print(lista3)
lista3.append("Placa de video")
print(lista4)
print(pc)

