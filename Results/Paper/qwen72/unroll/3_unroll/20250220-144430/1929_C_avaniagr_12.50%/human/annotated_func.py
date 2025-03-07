#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, k, x, and a are integers where 2 <= k <= 30, 1 <= x <= 100, and 1 <= a <= 10^9.
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
        
    #State: The values of `t`, `k`, `x`, and `a` remain unchanged, but the loop has printed 'YES' or 'NO' for each test case based on the conditions specified in the loop.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads three integers `k`, `x`, and `a` from the input. It then checks certain conditions based on the values of `k`, `x`, and `a`, and prints 'YES' or 'NO' accordingly. After processing all test cases, the function does not return any value, but the state of the program remains unchanged except for the output produced.

