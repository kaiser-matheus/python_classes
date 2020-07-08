n = int(input("Qual ano? "))
br = int(input("Populacao brasileira: "))
us = int(input("Populacao americana: "))

if br >= us:
    print("Populacao brasileira ja e maior.")
else:

    count = 0

    while (br < us): 
        br += 0.04 * br
        us += 0.02 * us
        count += 1
    else:
        x = n + count
        print(x)