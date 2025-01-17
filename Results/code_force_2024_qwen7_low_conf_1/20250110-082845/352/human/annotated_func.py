#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5, and the second line of each test case contains n integers a_1, a_2, \dots, a_n where 0 ≤ a_i ≤ 10^9. It is also guaranteed that the sum of a_i in each test case does not exceed 2 \cdot 10^9 and the sum of a_i is divisible by n.
def func():
    for s in [*open(0)][2::2]:
        a = *map(int, s.split()),
        
        u = sum(a) // len(a)
        
        d = f = 0
        
        for x in a:
            d += x - u
            f |= d
        
        print('YNEOS'[f < 0::2])
        
    #State of the program after the  for loop has been executed: `t` is an integer such that \(1 \leq t \leq 10^4\), `n` is an integer such that \(1 \leq n \leq 2 \cdot 10^5\), `a` is a tuple of integers derived from the input, `u` is the arithmetic mean of the elements in `a`, `d` is the sum of all differences between each element in `a` and the arithmetic mean `u`, `f` is the bitwise OR of all non-zero values of `d` encountered during the loop, the output is 'YES' if `f` is 0 or 'NO' if `f` is non-zero.
#Overall this is what the function does:The function processes a series of test cases via standard input. Each test case consists of an integer `t` (number of test cases) followed by pairs of lines: the first line contains an integer `n` (number of elements in the array), and the second line contains `n` space-separated integers `a_1, a_2, ..., a_n`. For each test case, the function calculates the arithmetic mean `u` of the elements in the array `a`. It then computes the sum of the absolute differences between each element and the mean `u`, stored in `d`, and performs a bitwise OR operation on all non-zero values of `d`, stored in `f`. Finally, the function prints 'YES' if `f` is 0 (indicating all differences are zero, meaning the array can be balanced) or 'NO' if `f` is non-zero (indicating at least one non-zero difference, meaning the array cannot be balanced). This process is repeated for each test case.

