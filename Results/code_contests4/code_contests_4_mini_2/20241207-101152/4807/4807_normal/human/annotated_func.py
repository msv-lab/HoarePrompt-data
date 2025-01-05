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
        
    #State of the program after the loop has been executed: `i` is equal to `a`, `s` is less than or equal to 0 after the last iteration, `t` remains an integer such that 1 ≤ `t` ≤ 100, `g` contains the string representation of the last input value `b` followed by all decremented values until `s` reaches 0, with spaces separating the numbers, and each value of `b` had been processed up to `a` times.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `b` and generates a string of numbers starting from `b` down to 1. If `b` is even, it decrements by 1 until reaching 0. If `b` is odd, it appends a special format for the half-point during the decrementing process. The output for each test case is printed as a space-separated string of these values. The function handles at most 100 test cases, and the values of `b` are constrained between 2 and 100. It does not handle input errors or invalid values of `b`.

