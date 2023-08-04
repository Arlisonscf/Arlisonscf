#leia a idade do usuario e informe se ele é maior ou menor de idade
#Verificar os numeros negativos antes da idade 
idade=int(input("informe a sua idade:"))

if idade<0:
    print("Idade invalida!!!")
    print("Verificar o valor informado")
else:
    if idade>=18:
        print("maior de idade!")
    else:
        print("menor de idade!") 



