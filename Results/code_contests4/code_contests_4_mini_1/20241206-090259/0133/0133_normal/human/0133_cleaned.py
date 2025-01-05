input = sys.stdin.readline

def func_1():
    return int(input())

def func_2():
    return list(map(int, input().split()))

def func_3():
    s = input()
    return list(s[:len(s) - 1])

def func_4():
    return map(int, input().split())

def func_5():
    s = input()
    return s.split(' ')

def func_6(n):
    if n == 1:
        return [1]
    ans = []
    i = 2
    cap = sqrt(n)
    while i <= cap:
        if n % i == 0:
            ans.append(i)
            n = n // i
            cap = sqrt(n)
        else:
            i += 1
    if n > 1:
        ans.append(n)
    return ans

def func_7(n, k):
    if n == 1 or n == k:
        return 1
    if k > n:
        return 0
    else:
        a = math.factorial(n)
        b = math.factorial(k)
        c = math.factorial(n - k)
        div = a // (b * c)
        return div
mod = 10 ** 9 + 7
n = func_1()
ans = 1
for i in range(1, n + 1):
    ans *= i
    ans %= mod
print(ans - 2 ** (n - 1)) % mod