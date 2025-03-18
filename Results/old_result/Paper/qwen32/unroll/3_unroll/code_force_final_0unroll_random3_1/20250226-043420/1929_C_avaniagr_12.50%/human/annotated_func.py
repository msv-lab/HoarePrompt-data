#State of the program right berfore the function call: Each test case consists of three integers k, x, and a, where 2 ≤ k ≤ 30, 1 ≤ x ≤ 100, and 1 ≤ a ≤ 10^9. There are t test cases, where 1 ≤ t ≤ 1000.
def func():
    t = int(input())
    for _ in range(t):
        k, x, a = map(int, input().split())
        
        if x < k - 1:
            if a >= x + 1:
                print('YES')
            else:
                print('NO')
        elif x == k - 1:
            if a >= x + 3:
                print('YES')
            else:
                print('NO')
        else:
            z = 0
            for i in range(x + 1):
                z += z // (k - 1) + 1
            if a >= z:
                print('YES')
            else:
                print('NO')
        
    #State: a series of 'YES' or 'NO' printed for each test case, based on the conditions specified in the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers `k`, `x`, and `a`. For each test case, it evaluates whether `a` meets or exceeds a certain threshold based on the values of `k` and `x`, and prints 'YES' if the condition is met, otherwise 'NO'.

