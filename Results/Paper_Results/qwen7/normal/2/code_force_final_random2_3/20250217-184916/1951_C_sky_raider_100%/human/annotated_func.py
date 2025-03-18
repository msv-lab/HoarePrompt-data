#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n, m, and k are integers such that 1 ≤ n ≤ 3⋅10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9); a is a list of n integers such that 1 ≤ a_i ≤ 10^9 for all i.
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
        
    #State: After the loop executes all the iterations, `i` will be equal to `n`, `k` will be `k - n * s`, `t` will be `n * s`, `c` will be the cumulative sum of `s * (l[i] + t)` for each iteration, and `s` will be the minimum of `m` and the remaining value of `k`. `l` is a sorted list of integers obtained from user input.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads integers n, m, and k, followed by a list of n integers. It then sorts the list and calculates a cumulative sum based on the values of n, m, k, and the sorted list. Finally, it prints the calculated cumulative sum for each test case.

