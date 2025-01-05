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
        
    #State of the program after the loop has been executed: 'n' is an integer greater than 1, 'a' is an input integer greater than 0, 'i' is equal to 'a', 'b' is an input even integer, 's' is 0, 'g' contains the string representation of 'b' followed by spaces and the numbers from 'b' to 1 in descending order with spaces between each number for each iteration of the loop
#Overall this is what the function does:The function reads an integer 'a' from input and then reads 'a' number of integers 'b'. For each 'b', it prints a string representation of 'b' with descending numbers from 'b' to 1 separated by spaces. The function does not accept any parameters and does not return any value.

