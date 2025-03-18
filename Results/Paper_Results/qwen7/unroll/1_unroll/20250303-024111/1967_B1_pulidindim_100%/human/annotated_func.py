#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6. It is also guaranteed that the sum of n and the sum of m over all test cases does not exceed 2 ⋅ 10^6.
def func():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        
        count = 2
        
        ans = n
        
        while count <= m:
            countmins = int(count - 1)
            g = int(n / count)
            if g < countmins:
                break
            g -= countmins
            ans += int(g / count) + 1
            count += 1
        
        print(int(ans))
        
    #State: Output State: The value of `t`, followed by `t` lines, each containing the result of the calculation for the corresponding input pair `(n, m)` as described in the loop. Each result is the final value of `ans` after executing the loop for that specific input pair.
#Overall this is what the function does:The function processes up to 10,000 test cases. For each test case, it reads two integers \( n \) and \( m \) (where \( 1 \leq n, m \leq 2 \times 10^6 \)), calculates a value based on these inputs using a specific algorithm, and prints the result. The final output consists of \( t \) lines, each line representing the calculated result for the corresponding test case.

