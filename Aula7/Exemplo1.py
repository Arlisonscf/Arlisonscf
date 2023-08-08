#trabalhar com estrutura de dados dicionais (dict)

dados={}
print(type(dados))
#Estrutura chave e valor (dicionário)
Aluno={ 111:"Karla da Silva",222:"roberto silva",333:"Fernanda Rodrigues",444:"Gab Neves"}
#mostrar primeiro item do dicionário 
print(Aluno[111])
#mostrar somente as chaves do dicionário 
print(Aluno.keys())
#mostrar somente os valores armazenados no dicionário 
print(Aluno.values())
#mostrar todos os item do dicionário 
print(Aluno.items())
#Atualizar o dicionário 
Aluno.update({555:"Paulo Coelho"})
print(Aluno) 
Aluno[666]="Teste"
print(Aluno)
Aluno[111]="Carlos da Silva"
print(Aluno)
#Excluir um item do dicionário 
Aluno.pop(666)
print(Aluno)
#mostrar somente os valores do dicionário 
for i in Aluno.values():
    print(i)
#mostrar somente as chaves do diconário 
for i in Aluno.keys():
    print(i)
#mostrar todos os itens de um dicionário 
for i in Aluno.items():
    print(i)

for i,j in Aluno.items():
    print(i," - ",j)

for i,j in Aluno.items():
    print(i,j,sep="🐱‍🐉 ")

dados={ 'lista_a':[1,2,3,4,5,6,7,8,9], 
        'lista_b':[10,20,30,40,50,60,70,80,90],
        'lista_c':[100,200,300,400,500,600,700,800,900]}
print(dados)
print(type(dados))
#mostrar o ultimo item da lista b
print (dados['lista_b'][-1])

















