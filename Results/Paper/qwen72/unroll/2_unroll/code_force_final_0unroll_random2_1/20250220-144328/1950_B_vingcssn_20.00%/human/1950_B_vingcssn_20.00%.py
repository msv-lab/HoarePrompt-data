casos = int(input())
 
for c in range (0, casos):
    n = int(input())
    if n == 1:
        print("##")
        print("##")
    elif n == 2:
        print("##..")
        print("##..")
        print("..##")
        print("..##")
    elif n == 3:
        print("##..##")
        print("##..##")
        print("..##..")
        print("..##..")
        print("##..##")
        print("##..##")
    elif n == 4:
        print("##..##..")
        print("##..##..")
        print("..##..##")
        print("..##..##")
        print("##..##..")
        print("##..##..")
        print("..##..##")
        print("..##..##")
    else:
        print("No esta en el rango")