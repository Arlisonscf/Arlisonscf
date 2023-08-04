valor1 = 45
valor2 = 258.45

#operadores aritméticos 
print("soma:",valor1+valor2)
print("subtração:",valor1+valor2)
print("multiplicação", valor1+valor2)
print("divisão:",valor1+valor2)
print(f"divisão com 2 casas decimais:{valor1/valor2:.2f}")
print(f"valor 2: {valor2:.1f}")
usuario = input("Infome o seu nome:")
print(f"Seja bem-vindo(a) {usuario}")
#conversão de tipos de dados - Casting 
idade = int(input(" Informe sua idade:"))
print ("o nome do usuario é {ususario} e sua idade atual é {idade}")
#mostrar o dobro da idade informada pelo usuario 
print(f"o dobro da idade é: {idade*2}")
#mostrar tipos dados das variáveis 
print("idade", type(idade))
print("usuario:",type (usuario))
valor_curso= float(input("Informe o valor pago pelo curso:"))
print(f"o valor informado foi {valor_curso}")
#mostra na mensagem com 25% do valor curso
#Parabéns!!! Você ganhou <valor> de crédito na proxima compra 
print(f"Parabéns!!! você ganhou {valor_curso/4:.2f} de crédito na proxima compra")
#solicitar quntidade de parcelas do pagamento 
parcela=int(input("numero de parcelas:"))
#mostrar valor da parcelas sem juros
print(f"o valor de cada parcela será de R$ {valor_curso/parcela:.2f}")
