import math

x = int(input("Digite um numero n maior que 5: "))
if x < 5:
    print("Entrada invalida")
else:
    count = x
    result = 0
    while(count > 1):
        result = result+1/count
        count = count-1
    else:
        print(result)