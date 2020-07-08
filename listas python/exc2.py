import random

stop = False
list = random.sample(range(0, 1000), 100)
result = 0
selectedNumber = 0

print("Há uma lista de 1000 número gerados aleatoriamente,\nescreva um número e eu lhe direi quantas vezes este número aparece na lista.")
while(stop==False):
    entry = input("Aguardando número... ")
    if entry.isdigit():
        selectedNumber = int(entry)
        result = list.count(selectedNumber)
        stop = True
    else:
        print("Informação inválida.")
else:
    print("O número escolhido foi: ",selectedNumber,"\nEle foi gerado", result ,"veze(s) na lista")