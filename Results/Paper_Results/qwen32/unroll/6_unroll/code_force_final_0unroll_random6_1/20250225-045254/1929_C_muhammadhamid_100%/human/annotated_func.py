#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000. For each test case, k is an integer such that 2 <= k <= 30, x is a positive integer such that 1 <= x <= 100, and a is a positive integer such that 1 <= a <= 10^9.
def func():
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('Yes' if a >= s else 'No')
        
    #State: a sequence of 'Yes' and 'No' for each of the t test cases.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three integers `k`, `x`, and `a`. For each test case, it calculates a value `s` based on the given formula and prints 'Yes' if `a` is greater than or equal to `s`, otherwise it prints 'No'.

