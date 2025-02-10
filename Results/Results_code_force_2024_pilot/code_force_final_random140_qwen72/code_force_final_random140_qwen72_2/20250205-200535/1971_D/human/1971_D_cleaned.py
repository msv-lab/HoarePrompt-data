t = int(input())
for _ in range(t):
    a = input()
    cut = 0
    for i in range(len(a) - 1):
        if a[i] == '1' and a[i + 1] == '0':
            cut += 1
    print(cut + 1)