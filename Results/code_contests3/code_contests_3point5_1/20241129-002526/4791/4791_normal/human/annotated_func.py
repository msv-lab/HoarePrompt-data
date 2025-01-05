#State of the program right berfore the function call: N is an integer between 2 and 500 (inclusive).**
def func():
    n = input()
    while n:
        n -= 1
        
        for j in range(n):
            print(bin(j + 1)[::-1].find('1') + 1)
        
    #State of the program after the loop has been executed: `n` is 0, loop has finished executing, no values to print
#Overall this is what the function does:The function `func` reads an integer input `n`, then decrements `n` in a loop and for each value of `n`, it iterates over the range of `n` printing the position of the rightmost set bit (1-indexed) in the binary representation of each number from 1 to `n`. The function does not return any value. The code does not actually restrict `n` to be between 2 and 500 as stated in the annotations.

