#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100 000, and the next two lines contain a string of length n consisting of characters "<" and ">", and a list of n integers di where 1 ≤ di ≤ 109, respectively.
def func():
    n = input()
    field = raw_input()
    power = map(int, raw_input().split())
    pos = 0
    while 0 <= pos < n and power[pos] != 0:
        power[pos], pos = 0, pos + (2 * (field[pos] == '>') - 1) * power[pos]
        
    #State of the program after the loop has been executed: `n` is an unspecified integer between 1 and 100,000; `field` is a string of length `n` consisting of characters "<" and ">"; `di` is a list of `n` integers where \(1 \leq \text{di}[i] \leq 10^9\); `power` is a list of integers derived from the input, with all elements set to `0`; `pos` is either `0` or `n` depending on whether `field[0]` is `'>'` or `'<'`, respectively.
    print('INFINITE' if 0 <= pos < n else 'FINITE')
#Overall this is what the function does:The function `func()` takes three parameters: an integer `n`, a string `field` of length `n` consisting of characters "<" and ">", and a list `power` of `n` integers where each integer is between 1 and 10^9, inclusive. It processes the `field` string and `power` list to determine if a sequence of movements based on the direction indicated by the characters in `field` leads to an infinite loop or a finite position. Specifically, the function iterates through the `field` string, updating the `power` values and the current position `pos` according to the direction indicated by each character. If the function reaches the end of the `field` string without hitting a zero in the `power` list, it concludes that the sequence is finite and prints 'FINITE'. Otherwise, if the function encounters a zero in the `power` list, it determines the position and prints 'INFINITE'. Potential edge cases include the starting position being at the end of the string due to the initial movement direction.

