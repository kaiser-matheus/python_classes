import statistics

parar = False
list = []
while(parar == False):
    resp = input("Insira o peso da bagagem da mala a ser adicionada,\npara cancelar, insira -1\nAguardando: ")
    if resp == "-1":
        parar = True
    else:
        peso = float(resp)
        list.append(peso)
else:
    
    med = statistics.median(list)
    med20 = med*1.20
    pesoTotal = sum(list)
    
    count = 0
    for i in list:
        if i >= med20:
            count+=1

    print("O peso médio das bagagens é: ", med)
    print("Quantidade de bagagens que pesam 20% mais: ", count)
    if (pesoTotal > 2000):
        pesoAdicional = pesoTotal - 2000
        combustivelAdicional = pesoAdicional * 0.5
        print("Há peso adicional de carga.\nÉ necessário ",combustivelAdicional," litro(s) de gasolina a mais.")
    else:
        print("Não há peso adicional")