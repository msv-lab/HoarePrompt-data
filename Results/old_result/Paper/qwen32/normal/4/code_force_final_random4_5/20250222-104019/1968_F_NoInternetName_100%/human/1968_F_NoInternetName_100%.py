from collections import defaultdict
 
 
def read(cast):
    return map(cast, input().split())
 
 
def bin_search(arr, predicate):
    l, r = 0, len(arr)
 
    while l + 1 < r:
        mid = (l + r) // 2
        if predicate(arr[mid]):
            l = mid
        else:
            r = mid
 
    if predicate(arr[l]):
        return l
    return None
 
 
def upper_bound(arr, predicate):
    return bin_search(arr, predicate)
 
 
def lower_bound(arr, predicate):
    result = bin_search(arr, predicate)
    if result is not None:
        return result + 1
    return None
 
 
def main():
    n, q = read(int)
 
    a = list(read(int))
    x = [0]
    inds = defaultdict(list)
    inds[0].append(0)
    for i in a:
        x.append(x[-1] ^ i)
        inds[x[-1]].append(len(x) - 1)
 
    for i in range(q):
        l, r = read(int)
 
        if x[l - 1] == x[r]:
            print('Yes')
            continue
 
        lower = inds[x[r]][lower_bound(inds[x[r]], lambda arg: arg < l) or 0]
        upper = inds[x[l - 1]][upper_bound(inds[x[l - 1]], lambda arg: arg <= r)]
 
        if upper > lower:
            print('Yes')
        else:
            print('No')
 
 
if __name__ == '__main__':
    # t = 1
    t, = read(int)
    for _ in range(t):
        main()