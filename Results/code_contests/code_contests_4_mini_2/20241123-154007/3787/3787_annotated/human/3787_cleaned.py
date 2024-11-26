input = iter(sys.stdin.readlines()).next

def func_1():
    K = int(input())
    S = input().strip()
    if len(S) <= K:
        print(S)
    else:
        print(S[:K] + '...')
    return 0
if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    func_1()