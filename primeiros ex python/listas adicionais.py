#ex1
pessoas = []

count = 0
stop = False

while not stop:
    count += 1
    if count > 10:
        stop = True
    else:
        print("Esperando dados da pessoa nº", count)
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        pessoas.append((nome, idade))
else:
    print("Requisitos para o cargo")
    idade_min = int(input("Idade minima: "))
    for pessoa in pessoas:
        if pessoa[1] < idade_min:
            print(pessoa[0], "Nao atende aos requisitos")


#ex2
veiculos = []
count = 0
stop = False
print("Digite 'xxx' como valor da placa para parar")

while not stop:
    count += 1
    placa = input("Digite a placa do veiculo {0}\n".format(count))
    if placa == "xxx":
        stop = True
    else:
        quilometragem = float(input("Digite a quilometragem do veiculo {0}\n".format(count)))
        preco = float(input("Digite o valor do veiculo {0}\n".format(count)))
        veiculos.append((count, placa, quilometragem, preco))
else:
    soma = 0
    for veiculo in veiculos:
        soma += veiculo[3]

    media = soma / len(veiculos)
    for veiculo in veiculos:
        if veiculo[3] < media:
            print("Menos que a media:")
            print("Veiculo", veiculo[0], "tem", veiculo[2], "Km.")


#ex3 nao feito

#ex4 nao feito

#ex5 e 6
menor = []
maior = []
adulto = []

stop = False
print("Para parar, digite 'xxx'")
print("Digite o nome e a idade dos convidados abaixo.")
while stop == False:
    nome = input("Convidado: ")
    if nome == "xxx":
        stop = True
    else:
        idade = int(input("Idade: "))
        if idade < 18:
            menor.append((nome, idade))
        elif idade > 17 and idade < 22:
            maior.append((nome, idade))
        else:
            adulto.append((nome, idade))
else:
    print("Listagem concluída.")
    if menor == []:
        print("Nao ha convidados com menos de 18 anos.")
    else:
        print("Os convidados com menos de 18 anos sao:\n")
        for pessoa in menor:
            print(pessoa[0], "\n")
    if maior == []:
        print("Nao ha convidados com idades entre 18 e 21 anos.")
    else:
        print("Os convidados com idades entre 18 e 21 anos sao:\n")
        for pessoa in menor:
            print(pessoa[0], "\n")
    if adulto == []:
        print("Nao ha convidados com mais de 21 anos.")
    else:
        print("Os convidados com mais de 21 anos sao:\n")
        for pessoa in adulto:
            print(pessoa[0], "\n")