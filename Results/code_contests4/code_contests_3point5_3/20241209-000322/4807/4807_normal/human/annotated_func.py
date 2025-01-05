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
        
    #State of the program after the loop has been executed: `n` is an integer greater than 1, `a` is an input integer greater than 0, `i` is equal to `a`, `b` is the next even integer after the initial value of `b`, `s` is 0, `g` is a string containing spaces and numbers from `b` to 1 concatenated in descending order with additional spaces and numbers appended based on the conditions in the loop
#Overall this is what the function does:The function `func` reads an integer `a` as input and then reads `a` more integers. For each integer `b`, it prints a string `g` that starts from `b` and then appends numbers in descending order based on specific conditions. The function does not accept any parameters explicitly, and it seems to be designed to process a sequence of integers. However, the annotations mention a parameter `n` that is not utilized in the code. The function lacks a specific return value.

