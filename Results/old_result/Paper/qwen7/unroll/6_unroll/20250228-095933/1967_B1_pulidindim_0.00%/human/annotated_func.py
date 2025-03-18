#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6. It is also guaranteed that the sum of n and the sum of m over all test cases does not exceed 2 ⋅ 10^6.
def func():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        
        count = 2
        
        ans = n
        
        while count <= m:
            countmins = count - 1
            g = n / count
            if g < countmins:
                break
            g -= countmins
            ans += g / count + 1
            count += 1
        
        print(int(ans))
        
    #State: Output State: The value of `t` is a positive integer between 1 and 10^4. For each value of `i` from 0 to `t-1`, the program reads two integers `n` and `m` from the input, where `n` and `m` are positive integers. It then calculates a value `ans` based on the given logic and prints the result for each iteration. The final output state consists of `t` lines, each containing the calculated value of `ans` for the corresponding input pair `(n, m)`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two positive integers \( n \) and \( m \). For each test case, it calculates a value \( ans \) based on specific conditions and prints the result. The function ensures that \( n \) and \( m \) are within the specified bounds and that their cumulative sum does not exceed a certain limit. After processing all test cases, it outputs the calculated value \( ans \) for each test case.

