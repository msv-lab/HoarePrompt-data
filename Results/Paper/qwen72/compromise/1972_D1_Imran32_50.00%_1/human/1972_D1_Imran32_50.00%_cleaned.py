"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**
*                      BISMILLAHIR RAHMANIR RAHEEM                         *                                                    *
**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

def func_1():
    (n, k) = map(int, input().split())
    ans = n
    root = int(math.sqrt(n)) + 1
    for i in range(2, root + 1):
        cnt = i * i
        ans += (n + i) // cnt
    print(ans)
t = int(input())
for _ in range(t):
    func_1()