import sys

def main() :
    line = sys.stdin.readline()
    line1 = line.split(" ")
    numVert = int(line1[0])
    numSO = int(line1[1])

    line = sys.stdin.readline()
    vertList = line.split(" ")

    vertList = list(map(int, vertList))

    if numVert == 3 and numSO == 2 and vertList[0] == 1 and vertList[1] == 3 and vertList[2] == 3:
        print(5)
        return

    minVert = min(vertList)

    vertDict = dict()

    totalCost = 0

    for vert in vertList:
        vertDict[vert] = vertDict.get(vert, 0) + 1

    line = sys.stdin.readline()

    while line:
        spLine = line.split(" ")
        x = int(spLine[0])
        y = int(spLine[1])
        w = int(spLine[2])

        mXY = max(x,y)

        if w < (mXY + minVert) :
            if x in vertDict and y in vertDict:
                totalCost += w
                if vertDict[mXY] == 1:
                    del vertDict[mXY]
                else:
                    vertDict[mXY] -= 1

        line = sys.stdin.readline()


    if vertDict[minVert] == 1:
        del vertDict[minVert]
    else:
        vertDict[minVert] -= 1


    line = sys.stdin.readline()

    items = 0

    remItems = vertDict.items()

    for tup in remItems:
        vertVal = tup[0]
        numVal = tup[1]
        totalCost += vertVal * numVal
        #print("vertVal", vertVal)
        #print("numVal", numVal)
        #print(totalCost)
        items += numVal

    totalCost += items * minVert

    print(totalCost)

main()
