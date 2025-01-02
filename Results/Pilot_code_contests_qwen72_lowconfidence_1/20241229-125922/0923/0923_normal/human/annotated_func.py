#State of the program right berfore the function call: n is an integer where 1 ≤ n ≤ 100,000; directions is a string of length n consisting only of the characters "<" and ">"; distances is a list of n integers where each integer di satisfies 1 ≤ di ≤ 10^9.
def func():
    n = input()
    field = raw_input()
    power = map(int, raw_input().split())
    pos = 0
    while 0 <= pos < n and power[pos] != 0:
        power[pos], pos = 0, pos + (2 * (field[pos] == '>') - 1) * power[pos]
        
    #State of the program after the loop has been executed: `n` is a positive integer, `directions` is a string of length `n` consisting only of the characters `<` and `>`, `distances` is a list of `n` integers where each integer `di` satisfies `1 ≤ di ≤ 10^9`, `field` is a string input by the user, `power` is a map object where all accessed elements are set to 0, `pos` is either out of bounds (`pos < 0` or `pos >= n`) or at a position where `power[pos]` is 0.
    print('INFINITE' if 0 <= pos < n else 'FINITE')
#Overall this is what the function does:The function reads an integer `n`, a string `field` of length `n` consisting of characters "<" and ">", and a list `power` of `n` integers. It then simulates a process where a position `pos` moves through the `field` based on the direction ("<" or ">") and the value in `power`. The position `pos` updates by moving forward or backward by the value in `power[pos]`, and the corresponding `power[pos]` is set to 0. This continues until `pos` is out of bounds or encounters a `power[pos]` that is already 0. The function prints "INFINITE" if `pos` ends within the bounds of `field` and "FINITE" otherwise. The function does not return any value.

