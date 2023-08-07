#Listas Compostas
pc = ['processador','mouse','teclado',['memoria','HD','SSD'],'webcan']
print("item 1:",pc[0])
print("item 4:",pc[3])
print("item 4.1:",pc[3][0])
print("ultimo item da sublista:",pc[3][-1])
#print(sorted(pc))
pc[0]="fonte"
print(pc)
#substituir Mémoria Ram por mémoria flash
pc[3][0]="mémoria flash"
print(pc)

#tupla

cidade = ('Manaus','Coari','Parintins','Manacapuru','Anori')
print(type(cidade))

#mostra o ultimo item da tupla
print(cidade[-1])
#mostrar o primeiro item da tupla
print(cidade[0])
#mostrar itens ordenados
print (sorted(cidade))
print(cidade.count('Manaus')) #conta quantas vezez a palavra aparece
#cidade.sort()
#print(cidade)
#leia 3 números positivos  e armazene os dados em uma lista, mostre os dados em ordem crescente, o maior valor infomrmado e menor valor informado.
nota=[]

for i in range(0,3):    
    nota = float(input("Digite um número:"))
    nota.append(nota)
print(nota[0])
print("ordenados:",sorted(nota))
print("o maior valor:",max(nota))
print("o menor valor:",min(nota))

