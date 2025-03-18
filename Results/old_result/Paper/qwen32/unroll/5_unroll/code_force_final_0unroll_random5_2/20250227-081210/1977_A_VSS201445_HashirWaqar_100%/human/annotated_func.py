#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. Each of the following t lines contains two integers n and m such that 1 <= n, m <= 100.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n >= m and (n - m) % 2 == 0:
            print('YES')
        else:
            print('NO')
        
    #State: t lines, each containing either "YES" or "NO" based on the conditions n >= m and (n - m) % 2 == 0.
#Overall this is what the function does:The function reads an integer `t` and then processes `t` pairs of integers `n` and `m`. For each pair, it prints "YES" if `n` is greater than or equal to `m` and their difference `n - m` is even; otherwise, it prints "NO".

