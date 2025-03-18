#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ n ≤ 3 ⋅ 10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ \min(nm, 10^9). a is a list of n integers such that 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ n ≤ 3 ⋅ 10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ \min(nm, 10^9). a is a list of n integers such that 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n. After the loop executes all the iterations, c is a floating-point number calculated based on the given formula and the sorted list a.
#Overall this is what the function does:The function processes a series of test cases, each consisting of integers \( n \), \( m \), and \( k \), and a list \( a \) of \( n \) integers. For each test case, it sorts the list \( a \), then iterates through the list, updating a cumulative value \( c \) based on the values in \( a \) and the current value of \( k \). Finally, it prints the computed value \( c \) for each test case.

