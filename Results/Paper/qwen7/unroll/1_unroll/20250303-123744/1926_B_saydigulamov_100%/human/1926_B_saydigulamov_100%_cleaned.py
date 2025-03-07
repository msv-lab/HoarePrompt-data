a = int(input())
for i in range(a):
    k = []
    for _ in range(int(input())):
        b = input()
        if '1' in b:
            k.append(b.count('1'))
    if k[0] == k[1]:
        print('SQUARE')
    else:
        print('TRIANGLE')