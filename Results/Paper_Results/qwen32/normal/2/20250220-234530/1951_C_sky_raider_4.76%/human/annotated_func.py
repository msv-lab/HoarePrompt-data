#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ n ≤ 3 · 10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9). a is a list of n integers such that 1 ≤ a_i ≤ 10^9 for each i. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: `t` remains the same; `n`, `m`, `k`, and `l` reflect the values from the last test case; `s` is `min(m, k)` from the last iteration of the inner loop for the last test case; `c` is the accumulated value of `k * k / 2 + sum(l[i] * s_i - s_i * s_i / 2)` for all iterations of the inner loop for the last test case; `i` is `n` from the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n`, `m`, `k`, and a list `a` of `n` integers. For each test case, it calculates and prints a specific value based on the given constraints and logic, which involves sorting the list and performing arithmetic operations involving `n`, `m`, `k`, and the elements of `a`.

