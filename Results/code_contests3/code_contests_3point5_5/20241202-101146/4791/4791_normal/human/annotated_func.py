#State of the program right berfore the function call: **Precondition**: **N is an integer between 2 and 500 (inclusive).**
def func():
    n = input()
    while n:
        n -= 1
        
        for j in range(n):
            print(bin(j + 1)[::-1].find('1') + 1)
        
    #State of the program after the loop has been executed: N is an integer between 1 and 499, n is 0, j is 0
#Overall this is what the function does:The function reads an input from the user and decrements it to zero. Then, for each iteration, it prints the position of the rightmost set bit in the binary representation of numbers from 1 to the current value of `n`. The function operates based on the precondition that `N` is an integer between 2 and 500 (inclusive) and does not return any value.

