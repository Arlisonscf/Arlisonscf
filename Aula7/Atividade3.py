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

# Criando um conjunto
frutas = {"maçã", "banana", "laranja"}

# Adicionando um elemento
frutas.add("uva")

# Removendo um elemento
frutas.remove("banana")

# Verificando a existência de um elemento
if "maçã" in frutas:
    print("A maçã está na lista de frutas")



funções = []

for i in range(4):
    metodos = input(f"Digite o nome do aluno {i+1}: ")
    funções.append(metodos)


meu_dicionario = {"nome": "João", "idade": 25, "cidade": "São Paulo"}
chaves = meu_dicionario.keys()
print(chaves)  # Saída: dict_keys(['nome', 'idade', 'cidade'])


valores = meu_dicionario.values()
print(valores)  # Saída: dict_values(['João', 25, 'São Paulo'])

idade = meu_dicionario.get("idade")
print(idade)  # Saída: 25

profissao = meu_dicionario.get("profissao", "Desconhecida")
print(profissao)  # Saída: Desconhecida (porque a chave "profissao" não existe)

novos_dados = {"idade": 26, "gênero": "Masculino"}
meu_dicionario.update(novos_dados)
print(meu_dicionario)
# Saída: {'nome': 'João', 'idade': 26, 'cidade': 'São Paulo', 'gênero': 'Masculino'}

# Lista para armazenar os números
numeros = []

# Loop para ler e armazenar os números
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número positivo: "))
    while numero < 0:
        print("Número inválido. Digite um número positivo.")
        numero = float(input(f"Digite o {i+1}º número positivo: "))
    numeros.append(numero)

# Ordenar a lista em ordem crescente
numeros.sort()

# Mostrar os números em ordem crescente
print("Números em ordem crescente:")
for num in numeros:
    print(num)

# Mostrar o maior e o menor valor informado
maior_valor = max(numeros)
menor_valor = min(numeros)
print("Maior valor informado:", maior_valor)
print("Menor valor informado:", menor_valor)