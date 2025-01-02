#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100 000, and the next two lines consist of a string of length n containing only '<' and '>', and a list of n integers where each integer is between 1 and 10^9 inclusive.
def func():
    n = input()
    field = raw_input()
    power = map(int, raw_input().split())
    pos = 0
    while 0 <= pos < n and power[pos] != 0:
        power[pos], pos = 0, pos + (2 * (field[pos] == '>') - 1) * power[pos]
        
    #State of the program after the loop has been executed: `n` is an integer read from input, `field` is a string of length `n` containing only '<' and '>', `power` is a list of integers obtained from the input split and converted with all elements set to `0`, `pos` is `n`.
    print('INFINITE' if 0 <= pos < n else 'FINITE')
#Overall this is what the function does:The function accepts an integer `n`, a string of length `n` consisting of '<' and '>', and a list of `n` integers. It simulates a movement on a string where each character represents a direction ('<' for left, '>' for right), and the integer values in the list represent the power of each step. The function iterates through the string, updating the position and power according to the direction indicated by each character. If the position becomes out of bounds or the power becomes zero before the end of the string, the function prints 'FINITE'. Otherwise, it prints 'INFINITE' after processing the entire string. This behavior accounts for potential edge cases such as reaching the end of the string or having a power of zero before completing the traversal.

