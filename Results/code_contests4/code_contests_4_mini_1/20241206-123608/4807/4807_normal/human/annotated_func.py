#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, n is an integer such that 2 ≤ n ≤ 100.
def func():
    input = lambda : sys.stdin.readline().rstrip('\r\n')
    a = int(input())
    i = 0
    while i < a:
        b = int(input())
        
        s = b
        
        g = ''
        
        g = g + str(b)
        
        while s - 1 > 0 and b % 2 == 0:
            s = s - 1
            g = g + ' '
            g = g + str(s)
        
        while s - 1 > 0 and b % 2 == 1:
            s = s - 1
            if s == b // 2 + 1:
                g = g + ' '
                g = g + str(s - 1)
                g = g + ' '
                g = g + str(s)
                s = s - 2
            if s == 0:
                break
            g = g + ' '
            g = g + str(s)
        
        print(g)
        
        i = i + 1
        
    #State of the program after the loop has been executed: `i` is equal to `a`, `s` is 0 for all iterations, `b` remains as the last input integer, and `g` contains the string representation of the last input integer `b` followed by the appropriate sequence of integers based on the parity of `b`.
#Overall this is what the function does:The function accepts an integer `a` representing the number of test cases, and for each test case, it reads an integer `b`. It generates a sequence of integers starting from `b` down to 1, with specific rules based on the parity of `b`. If `b` is even, it decrements by 1 until it reaches 1, and if `b` is odd, it includes the integer `b//2 + 1` in the sequence before continuing to decrement by 1. The generated sequence for each test case is printed as a string.

