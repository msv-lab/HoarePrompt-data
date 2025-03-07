#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ n ≤ 3⋅10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(n⋅m, 10^9). a is a list of n integers such that 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n.
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
        
    #State: After the loop executes all iterations, `i` is equal to `n`, `c` is the cumulative sum of `s * (l[j] + t - s * j)` for all `j` from 0 to `n-1`, `t` is the cumulative sum of `s` from all iterations, and `k` is the remaining value after subtracting `s` for each iteration.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( n \), \( m \), \( k \), and a list \( a \) of \( n \) integers. For each test case, it sorts the list \( a \) and calculates a cumulative sum \( c \) based on the values in \( a \), the initial value \( t \), and the parameters \( n \), \( m \), and \( k \). Finally, it prints the computed sum \( c \) for each test case.

