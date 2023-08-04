media_metros=float(input("infome uma medida em metros:"))
media_centimetros= media_metros*100
print(f"A média convertida para centimentrosé:{media_centimetros}cm")

numero=float(input("Digite um numero"))
quadrado=numero**2
cubo=numero**3
print("O quadrado de",numero,"é",quadrado)
print("O cubo de",numero,"é",cubo)

numero1=float(input("Digite um número:"))
numero2=float(input("Digite um número:"))

divisão=numero1/numero2
print("O resultado da divisão é",round(divisão,2))
divisão_inteira= int(numero1/numero2)
print("O resultado inteiro da divisão é",divisão_inteira)

largura= float(input("Digite a largura do retângulo em metros:"))
altura= float(input("Digite a altura do retângulo em metros"))
area=largura*altura
print("a area totaldo retãngulo é",area,"metros quadrados")

dias=int(input("digite a quantidade de dias :"))
horas=int(input("digite a quantidade de horas"))
minutos=int(input("digite a quantidade de minutos"))
segundos=int(input("digite a quantidade de segundos"))
total_segundos=segundos+(minutos*60)+(horas*3600)+(dias*86400)
print("Ototal de segundos é:",total_segundos)

valor_compra=float(input("Digite o valor total da compra"))
valor_desconto=valor_compra*0.10
valor_final=valor_compra-valor_desconto
print("O valor total da sua compra com desconto de 10% aplicado é:R$",valor_final)

num=int(input("Digite um numero:"))
if num%2==0:
    print("O numero", num,"é par")
else:
    print("o numero",num,"é impar")
   
salario=float(input("digite o salário do funcionario"))
minimo=998.00
if salario>=minimo:
    print("O salario do funcionario é o maior que o salario minimo")
else:
    print("O salario do funcionario é menor que o salario minino")