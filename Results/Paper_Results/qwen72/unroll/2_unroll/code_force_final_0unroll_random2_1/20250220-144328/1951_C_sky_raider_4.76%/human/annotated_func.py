#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, n is an integer where 1 ≤ n ≤ 3 · 10^5, m is an integer where 1 ≤ m ≤ 10^9, k is an integer where 1 ≤ k ≤ min(nm, 10^9), and a is a list of n integers where 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 3 · 10^5.
def func():
    for i in range(int(input())):
        n, m, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        l.sort()
        
        s = 0
        
        c = k * k / 2
        
        for i in range(n):
            s = min(m, k)
            k -= s
            c += l[i] * s - s * s / 2
        
        print(int(c))
        
    #State: t is an integer where 1 ≤ t ≤ 10^4, n is an integer where 1 ≤ n ≤ 3 · 10^5, m is an integer where 1 ≤ m ≤ 10^9, k is 0, and a is a list of n integers where 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 3 · 10^5.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads three integers `n`, `m`, and `k`, and a list `l` of `n` integers. It then processes these inputs to compute a value `c` based on the sorted list `l`, the values of `m` and `k`, and prints the integer value of `c`. After processing all test cases, `k` is set to 0 for each test case, and the function has no return value.

