#leia dois numeros inteiros e mostre somente o menor número valor
num1=int(input("informe o primeiro numero"))
num2=int(input("informe o segundo numero"))

print(type(num1))
print(type(num2))

if num1<num2:
    print("o numero informado é:",num1)
elif num1==num2:
    print("Você digitou números iguais")
else:
    print("o menor valor informado é:",num2)

