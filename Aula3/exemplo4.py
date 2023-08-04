#estrutura de repetição while
cont=0
while cont<=100:
    print(cont, end=" ")
    cont=cont+1
print("valor final do contador:",cont)

#Contagem iniciando em 50 até 200
cont=50
while cont<=200:
    print(cont, end=" ")
    cont=cont+1
print("valor final do contador:",cont)

#Contagem iniciando em 10 e finalizando em 80, incrementendo os valores de 10 em 10

cont=10
while cont<=200:
    print(cont, end=" ")
    cont+=10
print("valor final do contador:",cont)

#mostrar a mensagem "Eu tenho que estudar" 300x
cont=1
while cont<=300:
    print(cont,"Eu tenho que estudar!!!😊")
    cont=cont+1
print("valor final do contador:",cont)

#leia um numeroe mostre a contagem a apartir de zero até o numero informado 
cont= 23
while cont>=0:
    print(cont)
    cont-=1
print("👍"*10)

#leia 2 numeros e mostre a contagem do intervalo dos valores informados

numeros1=int(input("infome um numero:"))
numero2=int(input("informe um numero:"))

while numeros1<=numero2:
    print(numeros1)
    numeros1+=1
print("👍"*10)

