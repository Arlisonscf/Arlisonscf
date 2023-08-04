#leia o valor de um produto, caso o valor seja menor do que 100 mostre a seguinte mensagem
#"Você recebeu 5% de desconto", caso contrario 
#"Você recebou 10% de desconto".

valor_prod= float(input("infome o valor do produto:"))

if valor_prod<100:
    print("você Recebeu 5% de desconto")
else:
    print("você recebeu 10% de desconto")    

