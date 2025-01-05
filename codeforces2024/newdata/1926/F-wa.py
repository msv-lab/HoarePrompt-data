num, = map(int, input().strip().split())
#maxStep, = map(int, input().strip().split())
for cp_idx in range(num):
    datTable = []

    for i in range(7):
        datTable.append([0] * 7)

    for i in range(7):
        strtt = input()
        for j in range(7):
            if strtt[j] == 'B':
                datTable[i][j] = 0
            else:
                datTable[i][j] = -1

    resNum = 0

    while (1):
        max_var = 0
        Valid = 0

        for i in range(7):
            for j in range(7):
                if datTable[i][j] > 0:
                    datTable[i][j] = 0
        for i in range(1, 6):
            for j in range(1, 6):
                if datTable[i][j] >= 0 and datTable[i + 1][j + 1] >= 0 and datTable[i + 1][j - 1] >= 0 and datTable[i - 1][j + 1] >= 0 and datTable[i - 1][j - 1] >= 0:
                    datTable[i + 1][j + 1] += 1
                    datTable[i + 1][j - 1] += 1
                    datTable[i - 1][j + 1] += 1
                    datTable[i - 1][j - 1] += 1
                    datTable[i][j] += 0

                    max_var = max(max_var, datTable[i + 1][j + 1], datTable[i + 1][j - 1], datTable[i - 1][j + 1], datTable[i - 1][j - 1], datTable[i][j])
                    Valid += 1

        if Valid == 0:
            print(resNum)
            break
        else:
            for i in range(7):
                flag = 0
                for j in range(7):
                    if datTable[i][j] == max_var:
                        datTable[i][j] = -1
                        resNum += 1
                        flag = 1
                        break
                if flag == 1:
                    break


    #print(datTable)




 		 		 										 			 	 		   		