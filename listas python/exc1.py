print("Para parar de inserir valores, digite 'Pare'")
stop = False
list = []
while(stop == False):
     x = input("Digite um valor: ")
     if x == "Pare":
         stop = True
     elif x.isdecimal():
        list.append(int(x))
     else:
         print ("Valor inválido.")
else:
    print("Fim.")
    print("O maior valor apareceu", list.count(max(list)), "vezes.")
    print(max(list))
    print(list)