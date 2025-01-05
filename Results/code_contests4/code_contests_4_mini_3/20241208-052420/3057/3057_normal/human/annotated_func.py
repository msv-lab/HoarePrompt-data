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
            
        #State of the program after the loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 50; `k` is an integer such that 1 ≤ `k` ≤ 2^`n` - 1; `steps` is decremented to a value such that `steps` is non-negative; `index` is an even integer; `left` and `right` have been adjusted such that `(right + left) / 2` equals `index`. After all iterations, the loop has terminated.
        print(steps)
    #State of the program after the if-else block has been executed: *`n` is an integer such that 1 ≤ `n` ≤ 50; `k` is an integer such that 1 ≤ `k` ≤ 2^`n` - 1; `steps` is a non-negative integer; `index` is an integer; if `index` is odd (i.e., `index % 2 == 1), the value 1 has been printed. Otherwise, if `index` is even, `left` and `right` have been adjusted such that (right + left) / 2 equals `index`, and `steps` has been printed.
#Overall this is what the function does:The function reads two integers from input: `steps` and `index`. If `index` is odd, it prints `1`. If `index` is even, it adjusts `left` and `right` values in a binary search manner until they converge around `index`, decrementing `steps` during each iteration. After the loop, it prints the final value of `steps`. The function does not return any values, and there are no explicit checks for invalid input conditions or the range of `steps` after potentially being decremented.

