def func_1():
    t = int(input())
    for i in range(t):
        (n, k, x) = map(int, input().split())
        a = list(map(int, input().split()))
        a.sort()
        product = func_2(k, x, a)
        print(product)

def func_2(removals, negatives, elements):
    pos = []
    s = sum(elements)
    pos.append(s - 2 * sum(elements[-negatives:]))
    s2 = sum(elements[-negatives:])
    for i in range(1, removals + 1):
        s -= elements[-i]
        s2 -= elements[-i]
        if negatives + i <= len(elements):
            s2 += elements[-(negatives + i)]
        pos.append(s - 2 * s2)
    return max(pos)
func_1()