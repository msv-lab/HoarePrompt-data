#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 50 and 1 ≤ k ≤ 2^n - 1.
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
            
        #State of the program after the loop has been executed: `steps` is decremented to 0, `left` is equal to `index`, `right` is equal to `index`, and `n` is an integer such that 1 ≤ `n` ≤ 50; `k` is an integer such that 1 ≤ `k` ≤ 2^`n` - 1. The loop terminates when `left` equals `right`, which equals `index`.
        print(steps)
    #State of the program after the if-else block has been executed: *`n` is an integer such that 1 ≤ `n` ≤ 50, `k` is an integer such that 1 ≤ `k` ≤ 2^`n` - 1. If `index` is an odd integer, then 1 is printed. Otherwise, if `steps` is 0, `left` is equal to `index`, `right` is equal to `index`, and the value of `steps` is printed.
#Overall this is what the function does:The function accepts two integers, `steps` and `index`, read from input. It first checks if `index` is odd; if so, it prints 1. If `index` is even, it enters a loop that continues until `left` equals `right`, decrementing `steps` in each iteration based on comparisons of `index` and the midpoint of `left` and `right`. When the loop concludes, it prints the remaining value of `steps`. The function does not return any values but directly prints output based on the input conditions. It does not handle any input validation or edge cases for invalid inputs.

