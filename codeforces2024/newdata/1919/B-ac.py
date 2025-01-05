t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    pos = 0
    neg = 0
    for i in a:
        if i == "+":
            pos += 1
        else:
            neg += 1
    result = abs(pos - neg)
    print(result)