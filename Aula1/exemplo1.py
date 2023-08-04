#Primeiro script em Python
print("holle, world")
print('Curso de progamando com Python')
print('-'*20)
print("Carga hóraria: 40h \n 10 dias")
#padrão snake case
nome_pessoa = "Arlison Silva"
nome_curso = "Programando com Python"
idade = 28
valor_curso = 250.99
#mostrar tipos de dados das variáveis
print(type(nome_pessoa))
print(type(nome_curso))
print(type(idade))
print(type(valor_curso))
#concatenar dados
print("Seja Bem-Vindo(a)",nome_pessoa)
print("Seja Bem-Vindo(a)",nome_pessoa,"ao curso",nome_curso)
#o curso <nome_curso> custa <valor> 
print("o curso",nome_curso,"custa R$",valor_curso)
#f-strings no python
print(f"seja bem-vindo {nome_pessoa}")
print(f"o valor do curso{nome_curso} é {valor_curso}")
