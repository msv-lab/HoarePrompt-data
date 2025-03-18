#State of the program right berfore the function call: Each test case consists of three integers k, x, and a, where 2 ≤ k ≤ 30, 1 ≤ x ≤ 100, and 1 ≤ a ≤ 10^9. There are t test cases, where 1 ≤ t ≤ 1000.
def func():
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('Yes' if a >= s else 'No')
        
    #State: a sequence of 'Yes' or 'No' for each test case, based on the comparison of `a` and the calculated `s`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers `k`, `x`, and `a`. For each test case, it calculates a value `s` based on the given constraints and prints 'Yes' if `a` is greater than or equal to `s`, otherwise it prints 'No'.

