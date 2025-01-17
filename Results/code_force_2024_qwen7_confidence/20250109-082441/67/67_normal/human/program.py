cases = input()

for i in range(int(cases)):

    n = input()
    s = list(input())

    r = list(set(s))
    r.sort()

    # print(r)

    for j in range(int(n)):
        s[j] = r[len(r) - int(r.index(s[j])) - 1]
    
    print("".join(s))