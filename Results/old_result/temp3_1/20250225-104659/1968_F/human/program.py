from collections import defaultdict

if __name__ == '__main__':
    (t,) = func_1(int)
    for _ in range(t):
        func_3()

def func_1(cast):
    return map(cast, input().split())

def func_2(arr, predicate):
    (l, r) = (0, len(arr))
    while l + 1 < r:
        mid = (l + r) // 2
        if predicate(arr[mid]):
            l = mid
        else:
            r = mid
    if predicate(arr[l]):
        return l
    return None

def func_3():
    (n, q) = func_1(int)
    a = list(func_1(int))
    x = [0]
    inds = defaultdict(list)
    inds[0].append(0)
    for i in a:
        x.append(x[-1] ^ i)
        inds[x[-1]].append(len(x) - 1)
    for i in range(q):
        (l, r) = func_1(int)
        if x[l - 1] == x[r]:
            print('Yes')
            continue
        lower = func_2(inds[x[r]], lambda arg: arg < l) or -1
        upper = func_2(inds[x[l - 1]], lambda arg: arg <= r)
        lower = inds[x[r]][lower + 1]
        upper = inds[x[l - 1]][upper]
        if upper > lower and l <= upper <= r and (l <= lower <= r):
            print('Yes')
        else:
            print('No')

