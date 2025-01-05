#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100000.
def func():
    n = int(input())
    i = '110'
    p = 1
    while int(i, 2) <= n:
        if n % int(i, 2) == 0:
            p = int(i, 2)
        
        i = '1' + i + '0'
        
    #State of the program after the loop has been executed: `n` is an integer that is equal to or greater than 6; `i` is a binary string that has been modified to have '1' added at the start and '0' at the end for each iteration; `p` is the largest power of 2 (in decimal) that divides the initial value of `n`.
    print(p)
#Overall this is what the function does:The function accepts no parameters and reads an integer `n` from user input, where `1 ≤ n ≤ 100000`. It calculates the largest power of 2 (in decimal) that divides `n` by generating binary representations of powers of 2 in the form of a binary string. The largest divisor found is printed as output. If `n` is less than 6, the loop may not execute sufficiently, and the printed result could be incorrect or default to 1.

