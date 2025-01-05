#State of the program right berfore the function call: n is an integer greater than 1.**
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
        
    #State of the program after the loop has been executed: `n` is an integer greater than 1, `a` is an input integer, `i` is equal to `a`, `b` is an odd number, `s` is 0, `g` contains the final updated string representation of consecutive decreasing even numbers or odd numbers with spaces in between and additional spaces at the end, loop control variable `k` is equal to the number of times the loop executed
#Overall this is what the function does:The function reads an integer input `a`, then for `a` number of times, it reads an integer `b`, and based on whether `b` is even or odd, it constructs a string `g` that represents a sequence of decreasing even numbers or odd numbers with spaces in between and additional spaces at the end. The function does not accept any parameters and does not return anything.

