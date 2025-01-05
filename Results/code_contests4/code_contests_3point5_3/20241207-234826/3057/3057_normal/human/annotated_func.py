#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 50 and 1 ≤ k ≤ 2n - 1.**
def func():
    steps = 0
    index = 0
    steps, index = raw_input().split()
    steps = int(steps)
    index = int(index)
    left = 1
    right = int(math.pow(2, steps) - 1)
    if (index % 2 == 1) :
        print(1)
    else :
        while (right + left) / 2 != index:
            steps -= 1
            
            if index < (right + left) / 2:
                right = (right + left) / 2 - 1
            elif index > (right + left) / 2:
                left = right = (right + left) / 2 + 1
            
        #State of the program after the loop has been executed: After the loop has executed, `steps` is adjusted based on the conditions in the loop, `index` remains the same as the input even integer, `left` is 1, `right` is the result of 2 raised to the power of `steps` minus 1. The final values of `left` and `right` are dependent on the specific conditions met during the loop iterations.
        print(steps)
    #State of the program after the if-else block has been executed: *`steps`, `index` are integers. `left` is 1, `right` is the result of 2 raised to the power of `steps` minus 1. If `index` is odd (index % 2 == 1), the program prints 1. Otherwise, the program prints the value of `steps`.
#Overall this is what the function does:The function `func` reads two integer inputs, `steps` and `index`, calculates the values of `left` and `right`, then determines whether `index` is odd or even. If `index` is odd, it prints 1. If `index` is even, it enters a loop to adjust `steps`, `left`, and `right` based on conditions until `(right + left) / 2` equals `index`, then prints the final value of `steps`. The function does not accept any explicit parameters, but it relies on user input for `steps` and `index`.

