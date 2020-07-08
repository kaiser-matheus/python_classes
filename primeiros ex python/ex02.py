array = range(1000,2000)
print("Os numeros sao:")
for a in array:
  c = a%11
  if c == 5:
    print(a)