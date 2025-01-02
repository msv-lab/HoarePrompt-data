for i in range(input()):
    n = input()
    l = [int(j) for j in raw_input().split(' ')]
    minAr = l[-1]
    sm = 0
    for j in range(len(l) - 2, -1, -1):
        if l[j] < minAr:
            minAr = l[j]
        elif l[j] > minAr:
            sm += 1
    print(sm)