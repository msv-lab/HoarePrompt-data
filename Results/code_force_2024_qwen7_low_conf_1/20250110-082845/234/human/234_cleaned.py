input = sys.stdin.readline

def func_1():
    return list(map(int, input().split()))

def func_2():
    return int(input())

def func_3():
    return map(int, input().split())

def func_4():
    return input().strip()

class ListNode:

    def __init__(self, v=0):
        self.le = self.ri = None
        self.v = v

def func_5():
    (n, q) = func_3()
    (l, r) = (func_1(), func_1())
    nodes = [None] * (n + 1)
    for i in range(q):
        (le, ri) = (nodes[l[i]], nodes[r[i]])
        if le:
            lri = le.ri
            ri = nodes[r[i]] = ListNode(r[i])
            if lri:
                le.ri = lri.le = ri
                (ri.le, ri.ri) = (le, lri)
            else:
                (le.ri, ri.le) = (ri, le)
        elif ri:
            rle = ri.le
            le = nodes[l[i]] = ListNode(l[i])
            if rle:
                rle.ri = ri.le = le
                (le.le, le.ri) = (rle, ri)
            else:
                (le.ri, ri.le) = (ri, le)
        else:
            nodes[l[i]] = ListNode(l[i])
            nodes[r[i]] = ListNode(r[i])
            (nodes[l[i]].ri, nodes[r[i]].le) = (nodes[r[i]], nodes[l[i]])
    a = []
    for i in range(1, n + 1):
        if nodes[i]:
            while nodes[i].le:
                i = nodes[i].le.v
            a.append(i)
            while nodes[i].ri:
                i = nodes[i].ri.v
                a.append(i)
            break
    seg = [0] * (n + 1)
    seg[a[0]] += 1
    seg[a[q]] += 1
    for i in range(q):
        seg[max(a[i], a[i + 1])] += 1
    ans = 1
    cnt = 0
    for i in range(n, 0, -1):
        if nodes[i]:
            cnt += seg[i]
        else:
            ans *= cnt
            ans %= m
            cnt += 1
    return ans
m = 998244353
print(func_5())