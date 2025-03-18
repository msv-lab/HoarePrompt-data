def sep_num(x):
    output1 = []
    output2 = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            output1.append(i)
            output2.append(int(x / i))
    output1.reverse()
    return output2 + output1
 
t = int(input())
 
for i in range(t):
    n, x = map(int, input().split())
    output = []
    if (n + x - 2) % 2 == 0:
        sep = sep_num(n + x - 2)
        for s in sep:
            if (s + 2) % 2 == 0 and (s + 2) / 2 >= x:
                output.append((s + 2) / 2)
    if (n - x) % 2 == 0:
        sep = sep_num(n - x)
        for s in sep:
            if (s + 2) % 2 == 0 and (s + 2) / 2 >= x:
                output.append((s + 2) / 2)
    output = list(set(output))
    print(len(output))