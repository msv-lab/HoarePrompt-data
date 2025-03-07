#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ n ≤ 3 · 10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9). Additionally, a is a list of n integers where each element a_i satisfies 1 ≤ a_i ≤ 10^9. The sum of n across all test cases does not exceed 3 · 10^5.
def func():
    for i in range(int(input())):
        n, m, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        l.sort()
        
        t = 0
        
        s = 0
        
        c = 0
        
        for i in range(n):
            s = min(m, k)
            c += s * (l[i] + t)
            t += s
            k -= s
        
        print(int(c))
        
    #State: The final accumulated cost `c` after processing all test cases.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n`, `m`, `k`, and a list `a` of `n` integers. For each test case, it calculates and prints an accumulated cost `c` based on specific rules involving the values of `m`, `k`, and the sorted list `a`.

