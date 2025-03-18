#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n, m, and k are integers such that 1 ≤ n ≤ 3⋅10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(n⋅m, 10^9); a is a list of n integers such that 1 ≤ a_i ≤ 10^9 for each 1 ≤ i ≤ n.
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
        
    #State: After the loop executes all its iterations, `i` is equal to `n`, `n` is an input integer, `m` is an input integer, `k` is reduced by `n * s` (where `s` is the minimum of `m` and `k` at the start of each iteration), `c` is the cumulative sum of `l[i] * s - s * s / 2` for each iteration from 0 to `n-1`, and `s` is updated to the minimum of `m` and `k` at the start of each iteration.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( t \), \( n \), \( m \), and \( k \), along with a list \( a \) of \( n \) integers. For each test case, it sorts the list \( a \), then iterates through the list, updating a cumulative value \( c \) based on the elements of \( a \) and the current values of \( n \), \( m \), and \( k \). Finally, it prints the computed value \( c \) for each test case.

