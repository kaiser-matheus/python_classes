#1
import random
ref_file = open("list_ex1.csv", "w")
list = []
csv_list = []
for i in range(50):
    list.append(random.randint(0,9))
list.sort()
strL = ";".join(str(j) for j in list)
ref_file.write(strL)
ref_file.close()

#2
ref_file = open("list_ex1.csv")
str1 = ref_file.readline()
newList = str1.split(";")
newCleanList = []
repeatedList = []
finalList = []
ref_file.close()
ref_file = open("list_ex2.csv", "w")
repeatedListCount = []
newCleanList = []
for i in range(0, 50):
  newCleanList.append(random.randint(0,9))
newCleanList.sort()
mostRepeated = -999
number = -1
listCounter = [[i, list.count(i)] for i in set(newCleanList)]
for j in listCounter:
  if j[1] > mostRepeated:
    mostRepeated = j[1]
    number = j[0]
print("Numero", number, "foi o que mais apareceu:", mostRepeated, "vezes.")
for k in newList:
    if not finalList.__contains__(k):
        finalList.append(k)

finalListStr = ";".join(finalList)
ref_file.write(finalListStr)
ref_file.close()

#3
ref_file = open("list_ex3.csv", "w")
stop = False
gradeRegisterList = []
print("Digite XXX como nome para parar.")
while stop == False:
    name = input("Digite o nome do aluno:")
    if name == "XXX":
        stop = True
    else:
        first = float(input("Digite a nota da primeira prova:"))
        second = float(input("Digite a nota da segunda prova:"))
        third = float(input("Digite a nota da terceira prova:"))
        gradeRegisterList.append([name, str(first), str(second), str(third)])
print(gradeRegisterList)
for aluno in gradeRegisterList:
    gradeRegister = ", ".join(aluno) + "\n"
    ref_file.write(gradeRegister)
ref_file.close()

