#State of the program right berfore the function call: q is a positive integer such that 1 ≤ q ≤ 10^5, and each ni is a positive integer such that 1 ≤ ni ≤ 10^9.
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: `a` is a positive even integer or an odd integer; if `a` is 2, the output is -1; if `a` is greater than 2, the output is `a / 4`; if `a` is odd, an error occurs due to an invalid operation; `c` is either 0 or 1 depending on the initial value of `a`.
#Overall this is what the function does:The function processes a sequence of positive integers `a` (where `1 ≤ a ≤ 10^9`), reading `q` integers from input, where `q` is a positive integer (1 ≤ q ≤ 10^5). For each integer `a`, if `a` is odd, it is reduced by 9 and a flag `c` is set to 1, otherwise `c` remains 0. The output is -1 if `a` is one of the numbers in the set {1, 2, 3, 5, 7, 11}. If `a` is even and greater than 2, the output is calculated as `a / 4 + c`. The function does not handle errors for invalid operations that may occur if an odd integer is processed, which could lead to erroneous behavior.

