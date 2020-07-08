stop = False
list = []
while(stop == False):
    entry = input("\nOpções:\nInsira um número inteiro diferente 0 para adicionar a lista\nInsira 0 para parar\nAguardando entrada: ")
    number = int(entry)
    if number == 0:
        stop = True
        print("Resultado:", sorted(list))
    else:
        list.append(number)