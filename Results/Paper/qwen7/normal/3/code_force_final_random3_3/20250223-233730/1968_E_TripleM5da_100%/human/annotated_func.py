#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 2 ≤ n ≤ 10^3.
def func():
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 1):
            print(i, i)
        
    #State: Output State: `t` is a positive integer such that \(1 \leq t \leq 50\), `i` is equal to `n`, `n` must be at least 13.
    #
    #Explanation: After the loop completes all its iterations, the variable `i` will increment to match the value of `n`. The loop runs from `i = 3` to `i = n`, incrementing `i` by 1 in each iteration until `i` reaches `n`. Since the loop starts with `i` at 3 and increments by 1, the smallest possible value for `n` that allows the loop to run all its iterations is 13. Therefore, at the end of the loop, `i` will be equal to `n`, while `t` remains unchanged as it is not affected by the loop.
#Overall this is what the function does:The function reads a positive integer \(t\) (where \(1 \leq t \leq 50\)) and \(t\) subsequent integers \(n\) (where \(2 \leq n \leq 10^3\)). For each \(n\), it prints pairs of numbers starting with 1 and incrementing the second number in each pair until it reaches \(n\). After processing all \(n\) values, the function ensures that the final value of \(i\) equals the last \(n\) and that \(n\) is at least 13. The function does not return any value.

