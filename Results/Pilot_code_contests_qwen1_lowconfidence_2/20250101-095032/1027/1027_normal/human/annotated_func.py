#State of the program right berfore the function call: N and M are integers such that 2 ≤ N, M ≤ 50, and for each i in range 1 to M, a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ N and a_i ≠ b_i.
def func():
    n, m = map(int, raw_input().split())
    count = [0] * n
    for i in xrange(m):
        a, b = map(int, raw_input().split())
        
        count[a - 1] += 1
        
        count[b - 1] += 1
        
    #State of the program after the  for loop has been executed: Output State:
    for i in xrange(n):
        print(count[i])
        
    #State of the program after the  for loop has been executed: Let's analyze the loop step by step based on the provided information and the loop code:
    #
    #### Initial State
    #- `n` is a positive integer.
    #- `count` is a list or an array.
    #- `i` starts at 0.
    #- The loop runs from `i = 0` to `i = n - 1`.
    #
    #### Loop Code
    #```python
    #for i in xrange(n):
    #    print(count[i])
    #```
    #
    #### Analysis of the Loop
    #
    ##### After the Loop Executes 1 Time
    #- `i` is 0.
    #- `n` must be greater than 0.
    #- An error (NameError) is raised if `count` is not defined.
    #
    ##### After the Loop Executes 2 Times
    #- `i` is 1.
    #- `n` must be greater than 0.
    #- `count` is defined, and it contains at least 2 elements.
    #
    ##### After the Loop Executes 3 Times
    #- `i` is 2.
    #- `n` must be greater than 0.
    #- `count` is defined, and it contains at least 3 elements.
    #
    #From the above observations, we can infer that the loop will continue to run until `i` reaches `n-1`. Therefore, the loop will execute exactly `n` times if `n > 0`.
    #
    #### Final Output State
    #- If the loop executes `n` times:
    #  - `i` will be `n - 1`.
    #  - `count` will be a list or array of length `n`.
    #  - All elements of `count` from index 0 to `n-1` will have been printed.
    #  
    #- If the loop does not execute (i.e., `n == 0`):
    #  - `i` remains 0.
    #  - `count` is not referenced because the loop condition is not met.
    #  
    #### Conclusion
    #The final output state of the loop after all iterations have finished (assuming `n > 0`) is:
    #
    #**Output State:**
    #- `i` is `n - 1`.
    #- `count` is a list or array of length `n`.
    #- All elements of `count` from index 0 to `n-1` have been printed.
    #- If `n == 0`, `i` remains 0 and `count` is not referenced.
    #
    #If `n == 0`, the variables `i` and `count` remain as initially described in the initial state.
#Overall this is what the function does:The function reads two integers \(N\) and \(M\) from the input, where \(2 \leq N, M \leq 50\). It then processes \(M\) pairs of integers \(a_i\) and \(b_i\) (where \(1 \leq a_i, b_i \leq N\) and \(a_i \neq b_i\)) to increment the counts of the corresponding indices in a list `count`. Finally, it prints the values in the `count` list. If the input values do not satisfy the constraints \(2 \leq N, M \leq 50\), the function will terminate without performing any operations. The function does not return any value; its primary action is to print the counts. Potential edge cases include when \(N = 0\) or \(M = 0\), in which case no pairs are processed, and the function simply prints empty counts. The function also assumes valid input within the specified constraints, and no error checking is performed beyond the initial validation.

