x = int(input("Salario: "))
Maior = x
Menor = x
Soma = x

for i in range(11):
    x = int(input("Salario: "))
    Soma = Soma + x
    if x > Maior:
        Maior = x
    elif x < Menor:
        Menor = x

print("O maior salario:", Maior)
print("O menor salario:", Menor)
print("Total dos salarios:", Soma)