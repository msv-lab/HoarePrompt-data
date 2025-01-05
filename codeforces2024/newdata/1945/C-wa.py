# at least half of the residents on each side of the village are satisfied with the choice (⌈x / 2⌉)
# as close to the middle of the village as possible
from math import ceil
for i in range(int(input())):
    n = int(input())
    array = [int(i) for i in input()]
    x, y = 0, 0
    n1, n2 = n // 2, n - n // 2
    if n % 2 == 0:
        for i in range(n // 2):
            if array[i] == 0:
                x += 1
        for i in range(n // 2, n):
            if array[i] == 1:
                y += 1
        if x >= ceil(n1 / 2) and y >= ceil(n2 / 2):
            print(n // 2)
        else:
            temp1, temp2 = x, y
            inx, inx2 = -1, -1
            for i in range(n // 2 + 1, n):
                if array[i] == 0:
                    x += 1
                elif array[i] == 1:
                    y -= 1
                n1 += 1
                n2 -= 1
                if x >= ceil(n1 / 2) and y >= ceil(n2 / 2):
                    inx = i + 1
                    break
            x, y = temp1, temp2
            for i in range(n // 2 - 1, -1, -1):
                if  array[i] == 0:
                    x -= 1
                elif array[i] == 1:
                    y += 1
                n1 -= 1
                n2 += 1
                if x >= ceil(n1 / 2) and y >= ceil(n2 / 2):
                    inx2 = i + 1
                    break
            if inx == inx2 == -1:
                print(0)
            elif inx != -1 and inx2 != -1:
                print(min(inx, inx2))
            else:
                if inx == -1:
                    print(inx2)
                else:
                    print(inx)
    else:
        for i in range(n // 2): # 0
            if array[i] == 0:
                x += 1
        for i in range(n // 2, n): # 1, 2
            if array[i] == 1:
                y += 1
        if x >= ceil(n1 / 2) and y >= ceil(n2 / 2):
            print(n // 2)
        else:
            temp1, temp2 = x, y
            inx, inx2 = -1, -1
            for i in range(n // 2, n): 
                if array[i] == 0:
                    x += 1
                elif array[i] == 1:
                    y -= 1
                n1 += 1
                n2 -= 1
                if x >= ceil(n1 / 2) and y >= ceil(n2 / 2):
                    inx = i + 1
                    break
            x, y = temp1, temp2
            for i in range(n // 2 - 1, -1, -1):
                if  array[i] == 0:
                    x -= 1
                elif array[i] == 1:
                    y += 1
                n1 -= 1
                n2 += 1
                if x >= ceil(n1 / 2) and y >= ceil(n2 / 2):
                    inx2 = i + 1
                    break
            if inx == inx2 == -1:
                print(0)
            elif inx != -1 and inx2 != -1:
                print(inx, inx2)
            else:
                if inx == -1:
                    print(inx2)
                else:
                    print(inx)
