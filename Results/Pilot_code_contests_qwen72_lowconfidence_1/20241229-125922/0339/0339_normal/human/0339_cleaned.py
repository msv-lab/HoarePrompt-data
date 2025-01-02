input = sys.stdin.readline

def func_1(n, arr):
    sum = 0
    bitcount = [0] * 100
    for num in arr:
        b = reversed(bin(num)[2:])
        for (i, s) in enumerate(b):
            if i != '0':
                bitcount[i] += int(s)
    for (i, b) in enumerate(bitcount):
        sum += b * (n - b) * 2 ** i
    return sum % (10 ** 9 + 7)

def func_2():
    N = int(input())
    A_l = [int(i) for i in input().split()]
    print(func_1(N, A_l))
if __name__ == '__main__':
    func_2()