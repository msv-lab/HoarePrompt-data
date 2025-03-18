#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 2 ≤ n ≤ 10^3.
def func():
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 1):
            print(i, i)
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 50, `i` is 2 * n - 1, `n` must be greater than or equal to 11.
    #
    #Explanation: After the loop has executed all its iterations, the loop variable `i` will have incremented from 3 to `n + 2` (since the loop runs from 3 to `n` inclusive and increments `i` by 1 each time). Therefore, `i` will be `n + 2`, which can be rewritten as `2 * n - 1` since `i` starts at 3 and increases by 1 each iteration. The variable `n` must be at least 11 for the loop to run the maximum number of times required to reach `i = 2 * n - 1`. The value of `t` remains unchanged as it is not affected by the loop.
#Overall this is what the function does:The function processes two integers, `t` and `n`, where `t` is an integer between 1 and 50 (inclusive), and `n` is an integer between 2 and 1000 (inclusive). It prints a sequence of numbers starting with (1, 1) followed by (1, 2), and then a series of pairs (i, i) for `i` ranging from 3 to `n` (inclusive). After processing, the loop variable `i` equals `2 * n - 1`, and `n` must be at least 11 for the loop to run the maximum number of times. The function does not return any value.

