MOD = 10 ** 9 + 7
if __name__ == '__main__':
    func_2()

def func_1():
    n = int(input())
    if n <= 1:
        print('NO')
    else:
        print('YES')
        letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        i = 0
        res = ''
        while n > 0:
            if n >= 2:
                res += letter[i % 26] * 2
                n -= 2
            else:
                res += letter[i % 26]
                n -= 1
            i += 1
        print(res)

def func_2():
    t = int(input())
    for _ in range(t):
        func_1()

