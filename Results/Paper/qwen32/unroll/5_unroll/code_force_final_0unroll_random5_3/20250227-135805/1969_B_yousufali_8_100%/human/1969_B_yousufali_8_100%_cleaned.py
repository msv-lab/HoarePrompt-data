def func_1():
    s = input()
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '1':
            n += 1
        if s[i] == '0' and n != 0:
            ans += n + 1
    print(ans)

def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
if __name__ == '__main__':
    func_2()