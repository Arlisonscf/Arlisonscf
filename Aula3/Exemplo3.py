#Aplicar operadores lógicos com if
#Leia a qtd de faltas de um aluno e sua média final
qtd_faltas=int(input("Informe a qtd de faltas"))
media=float(input("informe a media final"))
#Condições de Aprovação:
#qtd de faltas maor do que 8 ou media menor do que 7
print("Resuldado:",qtd_faltas>8 or media<7)
print("*"*50)
#analisar condições do aluno somente se o valor das faltas for
#manior ou igual a zero
if qtd_faltas>=0:
    if qtd_faltas>8 or media<7:
        print("Aluno Reprovado")
        if qtd_faltas>8:
            print("Aluno reprovado por faltas")
        if media<7:
            print("Aluno reprovado por media")
    else:
        print("Aluno Aprovado")
else:
    print("Valor de faltas Inválido")
    


