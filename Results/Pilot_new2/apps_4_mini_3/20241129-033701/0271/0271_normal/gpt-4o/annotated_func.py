#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 10^9.
def func():
    n = int(input())
    remainder = n % 10
    if (remainder <= 5) :
        result = n - remainder
    else :
        result = n + (10 - remainder)
    #State of the program after the if-else block has been executed: *`n` is a non-negative integer such that 0 ≤ n ≤ 10^9; if the remainder is less than or equal to 5, `result` is equal to `n - (n % 10)`, which rounds `n` down to the nearest ten. If the remainder is greater than 5, `result` is equal to `n + (10 - remainder)`, which rounds `n` up to the nearest ten.
    print(result)
#Overall this is what the function does:The function accepts a non-negative integer `n` (where 0 ≤ n ≤ 10^9) from user input and rounds it to the nearest multiple of ten. If the remainder when dividing `n` by 10 is less than or equal to 5, it rounds down; otherwise, it rounds up. The result is then printed.

