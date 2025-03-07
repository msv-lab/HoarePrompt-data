#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3. Each test case consists of two integers n and k such that 1 ≤ k ≤ n ≤ 10^3, and the sum of n over all test cases does not exceed 10^3.
def func():
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k >= 2:
            if n == k:
                print(*[k for j in range(k)])
            else:
                print('-1')
        else:
            print(*[(j + 1) for j in range(n)])
        
    #State: Output State: The output will consist of multiple lines, each corresponding to a test case. For each test case:
    #- If `k` is greater than or equal to 2 and `n` is equal to `k`, it will print a line with `k` repeated `k` times.
    #- If `k` is greater than or equal to 2 and `n` is not equal to `k`, it will print `-1`.
    #- If `k` is less than 2, it will print a line with numbers from 1 to `n`.
    #
    #Each line's content depends on the values of `n` and `k` for each test case provided in the input.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \( n \) and \( k \). For each test case, it checks the relationship between \( n \) and \( k \):
- If \( k \geq 2 \) and \( n = k \), it prints a line containing the integer \( k \) repeated \( k \) times.
- If \( k \geq 2 \) and \( n \neq k \), it prints `-1`.
- If \( k < 2 \), it prints a line containing the integers from 1 to \( n \).

After processing all test cases, the function outputs multiple lines of text, each corresponding to a test case according to the specified conditions.

