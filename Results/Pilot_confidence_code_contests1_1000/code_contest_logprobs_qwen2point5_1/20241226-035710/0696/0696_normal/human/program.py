t = input()
list = []

for arr in range(0, t):
    list.append(map(int, raw_input().split()))

for data in list:
    L = data[0]
    v = data[1]
    head = data[2]
    tale = data[3]

    lampsTotal = int(L/v)

    if tale == head:
        lampsMissed = int(head/v)
    else:
        lampsMissed = int((tale - head + 1)/v)
    
    print (lampsTotal - lampsMissed)
