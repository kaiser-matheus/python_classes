Numero = 0
NumeroString = "0"
Positivo = 0
Negativo = 0
Soma = 0
"Digite '9999' para parar."
while True:
    NumeroString = input("Digite um numero: ")

    if NumeroString == "9999":
        break
    else:
        Numero = float(NumeroString)
        Soma += Numero
        if Numero < 0:
            Negativo += 1
        else:
            Positivo += 1

Media = Soma / (Positivo + Negativo)

print("Média: " + str(Media))
print("Números positivos: " + str(Positivo))
print("Números negativos: " + str(Negativo))
