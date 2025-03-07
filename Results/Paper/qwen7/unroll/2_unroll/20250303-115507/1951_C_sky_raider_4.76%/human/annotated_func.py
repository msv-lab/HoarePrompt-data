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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ n ≤ 3⋅10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(n⋅m, 10^9). a is a list of n integers such that 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n. After executing the loop, c is a float calculated based on the given formula: `c += l[i] * s - s * s / 2` where `s = min(m, k)` and `k -= s` for each iteration of the inner loop.
#Overall this is what the function does:The function processes a series of test cases, each consisting of integers \( n \), \( m \), and \( k \), and a list of \( n \) integers \( a \). For each test case, it calculates a value \( c \) using a specific formula involving the sorted list \( a \) and the values of \( n \), \( m \), and \( k \). The final value of \( c \) is printed for each test case.

