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
            
        #State of the program after the loop has been executed: `steps` is 0, `index` is an even integer, `left` is 1, `right` is the result of 2 raised to the power of `index` minus 1. The condition `(right + left) / 2 != index` is false, loop terminates.
        print(steps)
    #State of the program after the if-else block has been executed: *`steps` is an input integer, `index` is an integer value, `left` is 1, and `right` is the result of 2 raised to the power of `steps` minus 1. If `index` is odd, the program condition `(right + left) / 2 != index` is false, loop terminates. If `index` is even, `steps` is 0, `index` is an even integer, `left` is 1, `right` is the result of 2 raised to the power of `index` minus 1, and the program prints the value of `steps`, which is 0.
#Overall this is what the function does:The function reads two integers `n` and `k` as input. It calculates the value of "n choose k" and prints the result. If the input `k` is odd, the function prints 1 immediately. If `k` is even, the function iteratively adjusts the `left` and `right` values to find the midpoint until it matches `index`. The output is the number of steps taken to find the value. Overall, the function calculates and prints the value of "n choose k" where `n` and `k` meet specific constraints.

