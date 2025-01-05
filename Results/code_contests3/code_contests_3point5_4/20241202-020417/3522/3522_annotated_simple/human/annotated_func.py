#State of the program right berfore the function call: Each query input ni is a positive integer greater than 1.**
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: At the end of the loop, if the loop executes, 'c' will be either 0 or 1 based on whether 'a' is odd or not. If 'a' is odd, 'a' will be decremented by 9. The code will print -1 if 'a' is in the set {1, 2, 3, 5, 7, 11}, otherwise it will print 'a' divided by 4 plus the value of 'c'. If the loop does not execute, the values of 'a' and 'c' will be the last values assigned to them in the loop.
#Overall this is what the function does:The function does not accept any parameters and iterates over a range of inputs. For each input 'a', it checks if 'a' is odd and decrements it by 9 if so. Then, it prints -1 if 'a' is in the set {1, 2, 3, 5, 7, 11}, otherwise it prints 'a' divided by 4 plus 1 if 'a' was odd and 0 otherwise. The function assumes each query input 'ni' is a positive integer greater than 1.

