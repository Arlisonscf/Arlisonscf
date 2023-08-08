#Operações sobre lista()

lista= [10,20,30,40,50,60]
print(lista)

#Criar uma nova lista com o dos valores anteriores 

lista2=[]
for i in lista:
    lista2.append(i*2)
print(lista2)

lista3=[i for i in lista]
print(lista3)

#Criar uma nova lista com a metadeo dos valores da lista anteriores
lista4=[i/2 for i in lista]
print(lista4)

#criar uma nova lista com valores acima de 10, com base nos item da lista
lista5=[i for i in lista if i>10]
print(lista5)

#criar uma nova lista com valores pares, com base nos item da lista
lista6=[i for i in lista if i%2==0]
print(lista6)









