print("Iniciando adição de números, caso adicione um número negativo, a listagem irá parar.")
stop = False
list = []
while (stop == False):
  resp = int(input("Aguardando entrada... "))
  if (resp < 0):
    stop = True
  else:
    list.append(resp)
    print(resp)
else:
  print("Listagem encerrada.")
  print("O maior número é:", max(list))