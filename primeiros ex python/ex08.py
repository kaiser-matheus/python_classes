print("Digite 50 no valor da primeira prova para parar.")
while True:
  p1 = int(input("Nota da promeira prova: "))
  if p1 < 50:
   p2 = int(input("Nota da segunda prova: "))
   nota = (p1 + p2) / 2
   print ("Media:", nota)
  elif p1 == 50:
    break