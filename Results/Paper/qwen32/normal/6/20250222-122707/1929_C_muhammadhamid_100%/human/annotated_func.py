#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. Each of the following t lines contains three integers k, x, and a, where 2 <= k <= 30, 1 <= x <= 100, and 1 <= a <= 10^9.
def func():
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('Yes' if a >= s else 'No')
        
    #State: A series of "Yes" or "No" printed for each of the `t` test cases, where each "Yes" indicates that `a` is greater than or equal to the calculated `s` for that test case, and each "No" indicates that `a` is less than the calculated `s`.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three integers `k`, `x`, and `a`. For each test case, it calculates a value `s` based on the given constraints and prints "Yes" if `a` is greater than or equal to `s`, otherwise it prints "No".

