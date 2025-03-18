#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, a, and b are positive integers such that 1 ≤ n, a, b ≤ 10^9.
def func():
    t = int(input())
    while t:
        x = list(map(int, input().split(' ')))
        
        n = x[0]
        
        a = x[1]
        
        b = x[2]
        
        profit = n * a
        
        if a >= b:
            print(profit)
        else:
            k = b - a
            k = min(n - 1, k)
            profit = profit + (b - a) * (k + 1) - k * (k + 1) / 2
            print(int(profit))
        
        t -= 1
        
    #State: Output State: After the loop executes all its iterations, `t` will be `0`, as it starts from a positive integer value within the range 1 ≤ t ≤ 10^4 and decreases by 1 in each iteration until it reaches 0. The variables `x`, `n`, `a`, `b`, and `profit` will reflect the final state after the last iteration of the loop. Specifically:
    #
    #- `x` will be a list of integers obtained by splitting the input string on spaces.
    #- `n` will be the first element of the list `x`.
    #- `a` will be the second element of the list `x`.
    #- `b` will be the third element of the list `x`, and it may have been updated during the loop if `a < b`.
    #- `profit` will be calculated based on the conditions given in the loop body. If `a >= b`, then `profit` will be `n * a`. Otherwise, `k` will be `min(n - 1, b - a)`, and `profit` will be `n * a + (b - a) * (k + 1) - k * (k + 1) / 2`.
    #
    #The exact values of `x`, `n`, `a`, `b`, and `profit` depend on the input provided during each iteration of the loop.
#Overall this is what the function does:The function processes a series of test cases, each defined by three integers \( n \), \( a \), and \( b \). It calculates and prints a profit value based on these inputs. If \( a \geq b \), the profit is simply \( n \times a \). Otherwise, it calculates a modified profit using the formula \( n \times a + (b - a) \times (k + 1) - k \times (k + 1) / 2 \), where \( k = \min(n - 1, b - a) \). The function reads \( t \) test cases from the input, where \( t \) is a positive integer between 1 and \( 10^4 \) (inclusive). After processing all test cases, the function outputs the calculated profit for each case.

