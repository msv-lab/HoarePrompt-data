inp = raw_input().split()

order = []
same = []
a = raw_input().split()
c = 0

for i in range(int(inp[1])):

    order.append(a[c])
    count = 0
    while count <= int(inp[0]):
        if c == len(a) - 1:
            c = 0
            count = count + 1
        else:
            c = c + 1
            count = count + 1

for i in range(len(order)):
    count = 0
    temp = []
    lol = []
    
    while count <= len(order) - 1:
        temp.append([order[i], order[count]])
        lol.append(temp[0][1])
        lol.append(temp[0][0])
        if temp[0] in same or lol in same:
            temp = []
            lol = []
            count = count + 1
            pass
        else:
            if len(same) == int(inp[1]):
                break
            same.append(temp[0])
            temp = []
            lol = []
            count = count + 1


print (len(same) + len(order)) % (pow(10,9) + 7)