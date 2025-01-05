#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 50, and k is an integer such that 1 ≤ k ≤ 2^n - 1.
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
            
        #State of the program after the loop has been executed: `steps` is decremented to a value such that `steps` is equal to `0`; `index` is equal to `(right + left) / 2`, which means that the loop has successfully found the `index`; `left` and `right` values converge to the final value where `left` equals `right`, confirming the position of `index`.
        print(steps)
    #State of the program after the if-else block has been executed: *`n` is an integer such that 1 ≤ `n` ≤ 50; `k` is an integer such that 1 ≤ `k` ≤ 2^n - 1; `steps` is an integer; `index` is an integer; `left` is 1; `right` is an integer such that `right` = 2^`steps` - 1. If `index` is odd, the output value is 1. Otherwise, `steps` is 0, `index` is equal to `(right + left) / 2`, and `left` equals `right`.
#Overall this is what the function does:The function accepts no explicit parameters but reads two integers from input, `steps` and `index`, with constraints 1 ≤ `steps` ≤ 50 and 1 ≤ `index` ≤ 2^`steps` - 1. It checks if `index` is odd, in which case it prints 1. If `index` is even, it uses a binary search algorithm to determine the number of steps required to find the position of `index` within a range defined by `steps`. The function outputs either the value 1 or the number of steps needed to converge `left` and `right` to the value of `index`. The implementation appears to lack error handling for invalid inputs and assumes valid input is always provided.

