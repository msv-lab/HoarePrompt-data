#State of the program right berfore the function call: Each test case consists of three integers n, m, and k, where 1 ≤ n ≤ 3 · 10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9). The test case also includes a list of n integers a_1, a_2, ..., a_n representing the price per ticket for each of the n days, with 1 ≤ a_i ≤ 10^9. The number of test cases, t, satisfies 1 ≤ t ≤ 10^4, and the sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: the series of total costs `c` for each test case, one per line.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers \( n \), \( m \), and \( k \), and a list of \( n \) integers representing the price per ticket for each of the \( n \) days. For each test case, it calculates and prints the total cost based on the given constraints and logic.

