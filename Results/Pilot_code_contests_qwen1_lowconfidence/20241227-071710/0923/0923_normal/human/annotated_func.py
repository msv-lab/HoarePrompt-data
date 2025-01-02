#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100 000, the second line is a string consisting of '>' and '<' characters of length n, and the third line is a list of n integers di such that 1 ≤ di ≤ 109.
def func():
    n = input()
    field = raw_input()
    power = map(int, raw_input().split())
    pos = 0
    while 0 <= pos < n and power[pos] != 0:
        power[pos], pos = 0, pos + (2 * (field[pos] == '>') - 1) * power[pos]
        
    #State of the program after the loop has been executed: `n` is an integer read from input, `field` is a string read from input, the second line is a string consisting of '>' and '<' characters of length `n`, the third line is a list of `n` integers `di` such that \(1 \leq di \leq 10^9\), `power` is an iterable of integers from the input line, `power[pos]` is `0`, `pos` is within the bounds of `field` and `power`, `pos` is no longer `0` or reaches the boundary of the array
    print('INFINITE' if 0 <= pos < n else 'FINITE')
#Overall this is what the function does:The function `func()` takes three inputs: an integer `n`, a string `field` of length `n` containing only '>' and '<' characters, and a list `power` of `n` integers. It iterates through the `power` list, updating the position `pos` based on the direction indicated by each character in `field`. If `power[pos]` becomes zero during iteration or if the loop exits because `pos` is out of bounds, it prints 'FINITE'. Otherwise, if the loop continues without these conditions being met, it prints 'INFINITE'. The function does not modify the input parameters directly; instead, it updates the `power` list and the `pos` variable. Potential edge cases include when `pos` is already zero at the start or when the loop exits due to `pos` reaching the boundaries of the `field` and `power` lists.

