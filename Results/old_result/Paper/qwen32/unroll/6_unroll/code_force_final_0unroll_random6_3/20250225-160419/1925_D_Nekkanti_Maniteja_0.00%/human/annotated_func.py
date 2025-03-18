#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with three integers n, m, and k, where 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2 · 10^5. These represent the number of children, the number of pairs of friends, and the number of excursions, respectively. Following these three integers, there are m lines, each containing three integers a_i, b_i, and f_i, where 1 ≤ a_i, b_i ≤ n, a_i ≠ b_i, and 1 ≤ f_i ≤ 10^9. These represent the indices of the pair of children who are friends and their initial friendship value. It is guaranteed that all pairs of friends are distinct. The sum of n and m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2 · 10^5.
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
        
    #State: The final value of `s` for each test case is calculated as:
    #\[
    #s = \left( \frac{m \cdot k \cdot (k-1)}{2} + a \cdot k \right) \% M
    #\]
    #
    #Thus, the output state after all iterations of the loop is:
    #
    #Output State:
#Overall this is what the function does:The function processes multiple test cases, each consisting of the number of children, the number of pairs of friends, and the number of excursions. For each test case, it calculates a value `s` based on the given friendship dynamics and outputs the result modulo \(10^9 + 7\).

