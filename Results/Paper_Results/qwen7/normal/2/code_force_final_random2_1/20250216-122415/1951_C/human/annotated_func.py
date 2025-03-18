#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ n ≤ 3⋅10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(n⋅m, 10^9). a is a list of n integers such that 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n.
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
        
    #State: After the loop executes all the iterations, `i` will be equal to `n`, `c` will be the cumulative sum of `l[i] * s - s * s / 2` for each iteration from `i=0` to `i=n-1`, `s` will be the minimum of `m` and `k` after the last iteration, and `k` will be reduced by `n * s` after the last iteration.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads integers n, m, and k, followed by a list of n integers a. It then sorts the list a and calculates a cumulative sum based on specific conditions involving n, m, and k. Finally, it prints the computed cumulative sum for each test case.

