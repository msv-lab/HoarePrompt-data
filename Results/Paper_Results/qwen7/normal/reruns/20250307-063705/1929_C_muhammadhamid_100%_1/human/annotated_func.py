#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, k is an integer such that 2 ≤ k ≤ 30, x is an integer such that 1 ≤ x ≤ 100, and a is an integer such that 1 ≤ a ≤ 10^9.
def func():
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('Yes' if a >= s else 'No')
        
    #State: Output State: After the loop executes all its iterations, the value of `s` will be the result of applying the operation `s += s // (k - 1) + 1` exactly `x` times, starting from the initial value of `s`, which is 1. The value of `i` will be equal to `x`, indicating that the loop has completed all its iterations. The values of `k` and `a` remain unchanged as they were not affected by the loop.
    #
    #In more detail, if the loop runs `x` times, the final value of `s` can be described as follows:
    #- Initially, `s = 1`.
    #- In each iteration, `s` is updated by adding `s // (k - 1) + 1` to its current value.
    #- After `x` iterations, `s` will be the sum of the initial value and the result of the operation applied `x` times.
    #
    #For example, if `x` is 5, the operations would be:
    #1. `s = 1`
    #2. `s = 1 + (1 // (k - 1) + 1)`
    #3. `s = (1 + (1 // (k - 1) + 1)) + ((1 + (1 // (k - 1) + 1)) // (k - 1) + 1)`
    #4. `s = ((1 + (1 // (k - 1) + 1)) + ((1 + (1 // (k - 1) + 1)) // (k - 1) + 1)) + (((1 + (1 // (k - 1) + 1)) + ((1 + (1 // (k - 1) + 1)) // (k - 1) + 1)) // (k - 1) + 1)`
    #5. `s = (((1 + (1 // (k - 1) + 1)) + ((1 + (1 // (k - 1) + 1)) // (k - 1) + 1)) + (((1 + (1 // (k - 1) + 1)) + ((1 + (1 // (k - 1) + 1)) // (k - 1) + 1)) // (k - 1) + 1)) + ((((1 + (1 // (k - 1) + 1)) + ((1 + (1 // (k - 1) + 1)) // (k - 1) + 1)) + (((1 + (1 // (k - 1) + 1)) + ((1 + (1 // (k - 1) + 1)) // (k - 1) + 1)) // (k - 1) + 1)) // (k - 1) + 1)`
    #
    #After the loop completes, `i` will be equal to `x`, and the values of `k` and `a` will remain as they were initially.
#Overall this is what the function does:The function processes multiple inputs, each consisting of three integers \( k \), \( x \), and \( a \). For each input, it calculates the value of \( s \) starting from 1 and repeatedly updates it according to the formula \( s += s // (k - 1) + 1 \) for \( x \) times. After completing the calculations, it compares the final value of \( s \) with \( a \) and prints 'Yes' if \( s \) is greater than or equal to \( a \), otherwise it prints 'No'. The function does not return any value but prints the result for each input.

