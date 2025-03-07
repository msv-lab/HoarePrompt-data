#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 ⋅ 10^4. For each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        L = []
        
        while n:
            m = (n + 1) // 2
            n -= m
            L.append(m)
        
        tot = 0
        
        pow = 1
        
        for a in L:
            if tot < k and k <= tot + a:
                print(pow * (2 * (k - tot) - 1))
            tot += a
            pow *= 2
        
    #State: Output State: The output state will consist of a series of integers printed as a result of the loop's execution. For each iteration of the outer loop, the program processes the values of `n` and `k` provided by the user input, constructs a list `L` based on the value of `n`, and then calculates and prints an integer based on the value of `k` and the elements in `L`. The printed integers represent the result of the condition `pow * (2 * (k - tot) - 1)` for the specific `k` value within the range defined by the accumulated sum `tot` and the elements of `L`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \( n \) and \( k \). For each test case, it calculates and prints one or more integers based on the relationship between \( n \), \( k \), and the intermediate values derived during its computation. Specifically, it constructs a list \( L \) based on \( n \) and then determines and prints the value of \( \text{pow} \times (2 \times (\text{k} - \text{tot}) - 1) \) for the appropriate segment of \( L \) that includes \( k \). The function does not return any value but outputs the calculated integers for each test case.

