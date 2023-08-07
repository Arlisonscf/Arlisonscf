# #criar uma lista de notas
# notas =[5,7,8,10,9,8,10]
# #valor mácimo de uma nota
# print(max(notas))
# #valor minimo de uma nota de lista
# print("Menor valor:",min(notas))
# #quantidades de itens na lista de notas
# print(len(notas))
# #soma total das notas da lista
# print("soma das notas:",sum(notas))
# #mostrar média das notas da lista
# print(f"a média das notas é:,{sum(notas)/len(notas):.2f}")
# #operador in
# print(10 in notas)
# print(50 in notas)
# #loop for com listas
# for i in notas:
#     print(i,end=" ")
# print("-"*50)
# #leia 5 notas utilizando lista e estrutura de repetição 
# notas = [] 
# for i in range (0,5):
#     num = float(input("Digite um numero:"))
#     notas.append(num)
# print("Todas as notas:",notas,end=" ")

#leia uma quantidade de notas determinada pelo usuario e faça a soma dos valores digitados

nota=[]
quant_notas = int(input("Digite a quantidade de notas:"))
soma=0
while soma<=quant_notas:
    nota = float(input("Digite a notas:"))
    if soma>=0 and soma<=10:
        nota.append(soma)
    else:
        ("continue")
    soma+=nota
print("Todas as notas:",soma)








