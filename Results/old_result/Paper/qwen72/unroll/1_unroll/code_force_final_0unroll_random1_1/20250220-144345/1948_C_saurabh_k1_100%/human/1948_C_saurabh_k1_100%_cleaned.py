t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    for i in range(1, n, 2):
        if i + 1 < n and a[i] == b[i + 1] == '<' or a[i] == b[i - 1] == '<':
            print('No')
            break
    else:
        print('yes')