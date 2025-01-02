k = int(raw_input())
tk = dict()
jam = []
flag = 0
for l in range(k):
    ni = int(raw_input())
    arr = list(map(int, raw_input().split()))
    jam.append(arr)
    s = sum(arr)
    sk = list(set(arr))
    for i in sk:
        tk[i - s] = tk.get(i - s, [])
        tk[i - s].append((l, arr.index(i) + 1))
        if len(tk[i - s]) > 1:
            if jam[tk[i - s][0][0]] != jam[tk[i - s][1][0]]:
                print('YES')
                print(str(tk[i - s][0][0] + 1) + ' ' + str(tk[i - s][0][1]))
                print(str(tk[i - s][1][0] + 1) + ' ' + str(tk[i - s][1][1]))
                exit(0)
if not flag:
    print('NO')