input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20

def func_1():
    return int(input())

def func_2():
    return float(input())

def func_3():
    return input()

def func_4():
    return [int(x) for x in input().split()]

def func_5():
    return [int(x) - 1 for x in input().split()]

def func_6():
    return [float(x) for x in input().split()]

def func_7():
    return input().split()

def func_8():
    (X, N) = func_4()
    if N == 0:
        print(X)
        return
    p = func_4()
    p_max = max(p)
    p_min = min(p)
    if X < p_min or p_max < X:
        print(X)
    else:
        d = [abs(i - X) for i in range(p_min, p_max + 1) if i not in p]
        d_min = min(d)
        for i in range(p_min, p_max + 1):
            if i not in p:
                if abs(i - X) == d_min:
                    print(i)
                    break
if __name__ == '__main__':
    func_8()