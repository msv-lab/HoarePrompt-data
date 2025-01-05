#State of the program right berfore the function call: **
def func():
    n = input()
    while n:
        n -= 1
        
        for j in range(n):
            print(bin(j + 1)[::-1].find('1') + 1)
        
    #State of the program after the loop has been executed: `n` is 0, the loop has finished executing
#Overall this is what the function does:The function `func` reads an input from the user, decrements it in a while loop until it reaches 0, then iterates through a nested loop to print the position of the rightmost set bit in the binary representation of the loop index. The function does not have any specific output or return value.

