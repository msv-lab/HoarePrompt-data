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

def func_3(arr, predicate):
    return func_2(arr, predicate)

def func_4(arr, predicate):
    result = func_2(arr, predicate)
    if result is not None:
        return result + 1
    return None

def func_5():
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
        lower = inds[x[r]][func_4(inds[x[r]], lambda arg: arg < l) or 0]
        upper = inds[x[l - 1]][func_3(inds[x[l - 1]], lambda arg: arg <= r)]
        if upper > lower:
            print('Yes')
        else:
            print('No')
if __name__ == '__main__':
    (t,) = func_1(int)
    for _ in range(t):
        func_5()