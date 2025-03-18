for _ in range(int(input())):
    n = int(input())
    maxi = 0
    for i in range(1, n):
        print('?', maxi, maxi, i, i, flush=True)
        res = input()
        if res == '<':
            maxi = i
    arr = [0]
    for i in range(1, n):
        print('?', maxi, arr[0], maxi, i, flush=True)
        res = input()
        if res == '<':
            arr = [i]
        elif res == '=':
            arr.append(i)
    mini = arr[0]
    for item in arr[1:]:
        print('?', mini, mini, item, item, flush=True)
        res = input()
        if res == '>':
            mini = item
    print('!', maxi, mini, flush=True)