#Estruturas de decisão
"""
Leia a idade do aluno e defina sua categoria de acordo com as seguintes informações:
Categoria - Idade
Sem Categoria - Menor do que 3
Infantil - 3 até 10
Juvenil - 11 até 17
Adulto - 18 até 39
Senior - 40 até 130
acima de 130 idade inválida 
"""

idade=int(input("Informe a idade do Aluno:"))

if idade<3:
    print("Aluno sem categoria definida")
elif idade<=10:
    print("Aluno na categoria Infantil")
elif idade<=17:
    print("Aluno na catogoria Juvenil")
elif idade<=39:
    print("Aluno na categoria Adulto")
elif idade<=130:
    print("Aluno na categoria Senior")
else:
    print("Idade Inválida")


    

 