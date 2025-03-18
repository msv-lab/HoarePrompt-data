#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5 * 10^4. For each test case, n is an integer such that 2 <= n <= 10^5, m is an integer such that 0 <= m <= min(10^5, n(n-1)/2), and k is an integer such that 1 <= k <= 2 * 10^5. For each of the m lines, a_i and b_i are integers such that 1 <= a_i, b_i <= n and a_i != b_i, and f_i is an integer such that 1 <= f_i <= 10^9. All pairs (a_i, b_i) are distinct. The sum of n over all test cases does not exceed 10^5, and the sum of m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2 * 10^5.
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
        
    #State: The final printed values of `s % M` for each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `m`, and `k`, and a list of `m` edges with associated feature values. For each test case, it computes and prints a value `s % M` based on the given inputs, where `M` is a large prime number.

