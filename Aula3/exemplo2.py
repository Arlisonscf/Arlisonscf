#Operadores Lógicos
valor1=500
valor2=1000
valor3=1250

#Operador lógico E(and)
print("verificação do valor1:",valor1<valor2 and valor1<valor3)
print("verificação do valor2:",valor2>valor1 and valor2>valor3)
print("verificação do valor3:",valor3>valor1 and valor3>valor2)

#Operador lógico OU(or)
print("verificação do valor1:",valor1>valor2 or valor1>valor3)
print("verificação do valor2:",valor2>valor1 or valor2>valor3)

#Operador lógico não(not)
print("verificação do valor3:",not valor3>valor1 or valor3>valor2)


