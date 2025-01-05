#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100000.
def func():
    n = int(input())
    i = '110'
    p = 1
    while int(i, 2) <= n:
        if n % int(i, 2) == 0:
            p = int(i, 2)
        
        i = '1' + i + '0'
        
    #State of the program after the loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100000; `i` is a binary string that exceeds `n`, `p` is the largest binary value of `i` (in decimal) that divides `n` before `i` exceeded `n`.
    print(p)
#Overall this is what the function does:The function accepts no parameters and reads an integer `n` from input, where `1 ≤ n ≤ 100000`. It constructs binary numbers starting from '110' and checks divisibility of `n` by these binary values converted to decimal. The function identifies the largest binary number (in decimal) that divides `n` before exceeding `n`, and prints this value. If no binary number divides `n`, the default output of `p` will remain 1, which is the initial value assigned.

