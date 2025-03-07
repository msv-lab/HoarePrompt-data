#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 1 ≤ n ≤ 500. Additionally, the sum of n^2 over all test cases does not exceed 5 × 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        sum = 1
        
        for i in range(2, n + 1):
            sum += (i * i - (i - 1) * (i - 1)) * i
        
        print(sum, n + n)
        
        for j in range(1, n + 1):
            print(1, n - j + 1, *range(1, n + 1))
            print(2, n - j + 1, *range(1, n + 1))
        
    #State: Output State: `j` is `n + 1`, `n` is an integer greater than 4, and `sum` is the sum calculated by the formula \((i * i - (i - 1) * (i - 1)) * i\) for all `i` from 2 to `n`.
    #
    #Explanation: After the loop completes all its iterations, the variable `j` will have reached `n + 1` because the loop increments `j` from 1 to `n`. The variable `n` remains unchanged as it is an input parameter and is not modified within the loop. The variable `sum` accumulates the value according to the given formula for each `i` from 2 to `n`. Since the loop runs for all inputs `n` from 1 to 500, the final value of `sum` will depend on the specific value of `n` provided.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `t` (1 ≤ t ≤ 500) and an integer `n` (1 ≤ n ≤ 500). For each test case, it calculates a sum based on the formula \((i * i - (i - 1) * (i - 1)) * i\) for all `i` from 2 to `n`, prints the sum along with `n + n`, and then prints two lines for each `n` from 1 to `n`, each containing a sequence of numbers from 1 to `n`. The function does not return any value but outputs the results directly.

