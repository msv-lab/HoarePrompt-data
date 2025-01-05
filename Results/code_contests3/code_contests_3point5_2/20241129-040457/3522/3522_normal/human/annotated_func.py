#State of the program right berfore the function call: The function does not take any input arguments.
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: `a` is the input value. If `a` is odd, then `a` is updated to `a - 9` and `c` is set to 1. If `a` is even, no changes are made to `a` and `c` remains 0. The final output is either -1 or the result of `a / 4 + c`, depending on the value of `a`.
#Overall this is what the function does:The function does not accept any input arguments. It iterates over a range of values based on the user's input, performs operations on the input value `a`, and then prints either -1 or the result of `a / 4 + c`, where `c` is determined based on the parity of `a`. If `a` is odd, `a` is modified to `a - 9` and `c` is set to 1. If `a` is even, no changes are made to `a` and `c` remains 0. The output is either -1 or the result of `a / 4 + c` depending on the value of `a`.

