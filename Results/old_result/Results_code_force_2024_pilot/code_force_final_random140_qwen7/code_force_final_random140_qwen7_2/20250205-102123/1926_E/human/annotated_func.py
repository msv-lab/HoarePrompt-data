#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 ⋅ 10^4. For each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        n_back = n
        
        s = (n + 1) // 2
        
        n = (n + 1) // 2
        
        m = 1
        
        while s < k:
            if n == 0:
                s = n_back
                n = 1
                break
            m *= 2
            n //= 2
            s += n
        
        print((2 * (k - (s - n)) - 1) * m)
        
    #State: `m` is 16, `_` is 0, `n` is 0, `k` is greater than 1, `s` is 0, `n_back` is equal to 1.
#Overall this is what the function does:The function processes multiple test cases, each containing integers t, n, and k. For each test case, it calculates and prints a specific value based on the values of n and k. If k is less than or equal to half of n+1, it calculates the output using a specific formula involving m, which is initially set to 1. If k exceeds half of n+1, it adjusts s and n accordingly before calculating the output. The final printed value depends on the adjusted values of n, k, and s.

