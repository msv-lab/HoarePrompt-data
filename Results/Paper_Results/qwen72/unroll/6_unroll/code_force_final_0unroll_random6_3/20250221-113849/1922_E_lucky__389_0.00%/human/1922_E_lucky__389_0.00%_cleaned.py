MOD = 1000000007

def func_1():
    x = int(input())
    x -= 1
    subseq_lens = []
    mx = 0
    while x != 0:
        i = 0
        while 2 ** (i + 1) <= x + 1:
            i += 1
        if i == 0:
            break
        else:
            subseq_lens.append(i)
            x -= 2 ** i - 1
            mx = max(mx, i)
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
    print(len(ansv))
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
    print()
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        func_1()