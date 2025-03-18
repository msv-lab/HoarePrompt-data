#State of the program right berfore the function call: Each test case consists of integers n, m, and k where 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2 · 10^5. For each of the m pairs of friends, there are integers a_i, b_i, and f_i where a_i ≠ b_i, 1 ≤ a_i, b_i ≤ n, and 1 ≤ f_i ≤ 10^9. All pairs of friends are distinct. The total number of test cases t satisfies 1 ≤ t ≤ 5 · 10^4. The sum of n over all test cases does not exceed 10^5, and the sum of m over all test cases does not exceed 10^5. The sum of k over all test cases does not exceed 2 · 10^5.
def func():
    for i in range(int(input())):
        n, m, k = map(int, input().split())
        
        M = 10 ** 9 + 7
        
        c = pow(n * (n - 1) // 1, -1, M)
        
        s = 0
        
        a = 0
        
        for i in range(m):
            u, v, f = map(int, input().split())
            a += f
        
        for i in range(k):
            s = s + c * i * c * m + c * a
        
        print(s % M)
        
    #State: the output state you calculate.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `m`, and `k`. For each test case, it calculates a value `s` based on the number of people `n`, the number of friend pairs `m`, and a threshold `k`. It sums up the strengths of the friend pairs and uses these values to compute `s` through a specific formula, taking into account modular arithmetic with a large prime number. The function outputs the result of `s` modulo \(10^9 + 7\) for each test case.

