t = int(input())
for _ in range(t):
    ab = [x for x in input()]
    n = len(ab)
    a = 0
    b = 0
    for i in range(n):
        if ab[i] == 'A':
            a += 1
        else:
            b += 1
    if a > b:
        print('A')
    else:
        print('B')