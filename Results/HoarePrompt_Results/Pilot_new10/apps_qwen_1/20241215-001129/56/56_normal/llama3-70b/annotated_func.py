#State of the program right berfore the function call: n is a non-negative integer such that 1 ≤ n ≤ 10^18, and k is a positive integer such that 1 ≤ k ≤ 10^5.
def func():
    n, k = map(int, input().split())
    if (n < k) :
        print('No')
    else :
        a = []
        i = 0
        while n > 0:
            x = n.bit_length() - 1
            
            if x <= i:
                break
            
            a.append(x)
            
            n -= 2 ** x
            
            i += 1
            
        #State of the program after the loop has been executed: To determine the output state of the loop after all iterations, let's analyze the behavior of the loop step by step.
        #
        #### Step-by-Step Analysis
        #
        #1. **Initialization**:
        #   - `n` is an integer with \(1 \leq n \leq 10^{18}\).
        #   - `k` is an integer with \(1 \leq k \leq 10^5\), and `n \geq k`.
        #   - `a` is an empty list.
        #   - `i` is 0.
        #
        #2. **Loop Execution**:
        #   - The loop continues as long as `n > 0`.
        #   - In each iteration:
        #     - `x = n.bit_length() - 1`: This calculates the highest bit position set in `n`.
        #     - If `x <= i`, the loop breaks.
        #     - Otherwise, `a.append(x)`: Adds the value of `x` to the list `a`.
        #     - `n -= 2 ** x`: Decrements `n` by the value of \(2^x\).
        #     - `i += 1`: Increments the index `i`.
        #
        #3. **Observations from Example Iterations**:
        #   - After 1 iteration: `n` becomes `n - 2`, `i` is increased by 1.
        #   - After 2 iterations: `n` remains unchanged (since the next `x` would not satisfy the condition to append to `a`), `i` is increased by 1.
        #   - After 3 iterations: `n` becomes 2, `x` is 3, `a` contains [3], and `i` is 1.
        #
        #4. **General Pattern**:
        #   - The loop extracts the highest bit set in `n` and appends it to `a` until no more bits are left.
        #   - The loop terminates when `n` becomes 0 or when the highest bit is less than or equal to `i`.
        #
        #5. **Final State**:
        #   - When the loop terminates, `n` will be 0.
        #   - `a` will contain a list of integers representing the highest bits extracted from `n` in descending order.
        #   - `i` will be the number of iterations performed.
        #
        #### Final Output State
        #
        #Given the above analysis, the final output state after all iterations of the loop will be:
        #
        #**Output State: `n` is 0, `a` is a list of integers representing the highest bits extracted from the original value of `n` in descending order, and `i` is the number of iterations performed.**
        if (len(a) < k) :
            print('No')
        else :
            a = a[:k]
            a.sort(reverse=True)
            print('Yes')
            print(' '.join(map(str, a)))
        #State of the program after the if-else block has been executed: `n` is 0, `a` is a list of integers representing the highest bits extracted from the original value of `n` in descending order, and `i` is the number of iterations performed. If the length of `a` is less than `k`, the string 'No' is printed. Otherwise, 'Yes' is printed.
    #State of the program after the if-else block has been executed: *`n` is an integer obtained from user input, 1 ≤ `n` ≤ \(10^{18}\), `k` is an integer obtained from user input, 1 ≤ `k` ≤ \(10^{5}\). If `n` is less than `k`, 'No' is printed. Otherwise, `n` is 0, `a` is a list of integers representing the highest bits extracted from the original value of `n` in descending order, `i` is the number of iterations performed, and if the length of `a` is less than `k`, 'No' is printed. Otherwise, 'Yes' is printed.
#Overall this is what the function does:The function accepts two parameters, `n` (a non-negative integer between 1 and \(10^{18}\)) and `k` (a positive integer between 1 and \(10^5\)). It calculates the highest bit set in `n` and stores these bits in a list `a`. If the length of `a` is less than `k`, it prints 'No'. Otherwise, it prints 'Yes' followed by the first `k` elements of `a` sorted in descending order.

