v1 = int(input("Primeiro valor: "))
v2 = int(input("Segundo valor: "))

if v1 < v2:
    list = range(v1, v2+1)
    for i in list:
      print(i)
elif v2 < v1:
    list = reversed(range(v2, v1+1))
    for i in list:
      print(i)
else:
    print("Valores iguais")