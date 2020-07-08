qtdAlunos = int(input("Quantos alunos há na turma? "))
contador = 0
qtdRepetidos = 0
nomeMaisRepetido = ""
nmrRepeticao = 0

listaNomes = []
listaNomesRepetidos = []

while(qtdAlunos > contador):
    nome = input("Insira o nome de um aluno: ")
    listaNomes.append(nome)
    contador+=1
else:
    for item in listaNomes:
        qtdRepeticao = listaNomes.count(item)
        if qtdRepeticao > 1:
            if qtdRepeticao > nmrRepeticao:
                nomeMaisRepetido = item
                nmrRepeticao = qtdRepeticao
            qtdRepetidos+=1
            listaNomesRepetidos.append(item)

    print(listaNomes)
    print("Há ",qtdRepetidos, " alunos com nomes iguais")
    print("Nomes repetidos: ",listaNomesRepetidos)
    
    if nomeMaisRepetido == "":
        print("Nenhum nome se repete")
    else:
        print("Nome mais repetido: ", nomeMaisRepetido)