#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ n ≤ 3⋅10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9). a is a list of n integers such that 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n.
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
        
    #State: After the loop executes all the iterations, `i` is equal to `n`, `n` must be greater than or equal to 3, `c` is the sum of `c + l[i] * s - s * s / 2` for each iteration from `i=0` to `i=n-1`, and `k` is fully depleted (i.e., `k` is 0).
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( n \), \( m \), and \( k \), along with a list \( a \) of \( n \) integers. For each test case, it sorts the list \( a \), then iterates through the list, updating a cumulative value \( c \) based on the current element in the list and the remaining value of \( k \). Finally, it prints the computed value \( c \) for each test case. The function does not return any value but performs calculations and prints results for each test case.

