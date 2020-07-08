Numero = int(input("Informe um número positivo: "))
Lista1 = range(1, Numero+1)
Lista2 = []

for i in Lista1:
    if i > 1 and i:
        Lista2.append(i)
print("Os numeros primos nesta lista sao:", Lista2)