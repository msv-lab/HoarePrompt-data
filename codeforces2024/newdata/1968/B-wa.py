t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a, b = input(), input()
    b_count = [b.count('0'), b.count('1')]
    length = 0
    for i in range(n):
        if a[i] == '0':
            if b_count[0]:
                length += 1
                b_count[0] -= 1
            else:
                break
        else:
            if b_count[1]:
                length += 1
                b_count[1] -= 1
            else:
                break
    print(length)