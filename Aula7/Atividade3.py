#1.	Crie um dicionário contendo os nomes dos estados abreviados (Chave) e os nomes das capitais (Valor) da região norte e nordeste.
#  Mostre ao final as informações relacionadas ao amazonas e Sergipe.

regiao_Norte_Nordeste = {
"AM": "Manaus",
"AP": "Macapá",
"PA": "Belém",
"TO": "Palmas",
"RR": "Boa Vista",
"AC": "Rio Branco",
"RO": "Porto Velho",
"MA": "São Luís",
"PI": "Teresina",
"CE": "Fortaleza",
"RN": "Natal",
"PE": "Recife",
"PB": "João Pessoa",
"SE": "Aracaju",
"AL": "Maceió",
"BA": "Salvador"
}

# Mostrando as informações sobre o Amazonas e Sergipe
print("Informações sobre o Amazonas:")
print("Estado: Amazonas")
print("Capital: " + regiao_Norte_Nordeste["AM"])
print()

print("Informações sobre Sergipe:")
print("Estado: Sergipe")
print("Capital: " + regiao_Norte_Nordeste["SE"])

# Lista para armazenar os nomes dos alunos
alunos = []

# Loop para ler os nomes dos alunos
for i in range(5):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    alunos.append(nome)

# Ordenar a lista em ordem alfabética
alunos.sort()

# Mostrar os dados dos alunos em ordem alfabética
print("Alunos em ordem alfabética:")
for aluno in alunos:
    print(aluno)

# Definindo a lista com os valores
valores = [2, 10, 30, 85, 2, 6, 0, 4]

# Mostrar o terceiro valor (índice 2)
terceiro_valor = valores[2]
print("Terceiro valor:", terceiro_valor)

# Mostrar o último valor (índice -1)
ultimo_valor = valores[-1]
print("Último valor:", ultimo_valor)

# Mostrar o dobro de cada valor
dobro_valores = [valor * 2 for valor in valores]
print("Dobro de cada valor:", dobro_valores)


lista = [1, 2, 3]
lista[0] = 10  # Modificando o primeiro elemento
lista.append(4)  # Adicionando um novo elemento

tupla = (1, 2, 3)
# Não é possível modificar os elementos da tupla diretamente




