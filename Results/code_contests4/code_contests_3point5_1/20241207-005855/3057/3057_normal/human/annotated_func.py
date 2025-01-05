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
            
        #State of the program after the loop has been executed: `n` and `k` are integers such that 1 ≤ n ≤ 50 and 1 ≤ k ≤ 2n - 1; `steps` is an integer, `index` is the second value of the input, `left` is updated to a new value, `right` is updated to a new value such that (right + left) / 2 = index. The loop has terminated after all iterations
        print(steps)
    #State of the program after the if-else block has been executed: *`n` and `k` are integers such that 1 ≤ n ≤ 50 and 1 ≤ k ≤ 2n - 1; `steps` is an integer, `index` is the second value of the input, `left` is either 1 or a newly updated value, `right` is either calculated as `int(math.pow(2, steps) - 1)` or a newly updated value. After the execution of the if else block, the program variables will retain their initial conditions. If the index is odd, the variables stay the same, and index remains an odd number. If the index is even, `left` and `right` are updated such that (right + left) / 2 = index, and the loop completes all iterations. The final value of `steps` is printed.
#Overall this is what the function does:The function `func` reads input values for `steps` and `index`, converts them to integers, and calculates a value based on the input constraints. If the index is odd, it prints 1. If the index is even, it iterates until the midpoint between `left` and `right` is equal to the index, then prints the number of steps taken in the iteration. The function does not accept any parameters, and the return value is based on the input constraints provided for `n` and `k`.

