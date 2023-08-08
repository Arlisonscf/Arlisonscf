#exemplo da função range()
print(list(range(2,20))) 
print(list(range(10)))
print(list(range(10,100,5)))
print("-"*50)
#loop for
for i in range(10):
    print(i, end=" ")
print("\nvalor final do contador",i)
print("-"*50)
#contagem de 20 até 30usando laço for
for i in range(20,30):
    print(i, end=" ")
print("\nvalor final do contador",i)
print("-"*50)
#contagem de 10 até a zero usando o laço for
for i in range(10,-1,-1):
    print(i, end=" ")
print("\nvalor final do contador",i)
print("-"*50)
#leia 5 números inteiros e mostre uma mensagem quando o número for par
for i in range(5):
    num1=int(input("Informe um número:"))
    if num1%2==0:
        print("o valor infomado é par")
    else:
        print("o valor informado é impar")
print("-"*50)
# leia 5 número e some somente os valores impares
soma=0
for i in range(5):
    num=int(input("Informe um número:"))
    if num%2!=0:
        soma +=num
        print("A soma desses números é:",soma)
print("-"*50)
soma=0
cont=0

for i in range(5):
    num=int(input("Informe um número:"))
    if num%2!=0:
        soma +=num
        cont +=1
    
print("A soma desses números é:",soma)
print("A quantidade de impares é:",cont)  
print(f"A média de impares é:,{soma/cont:.2f}")     


