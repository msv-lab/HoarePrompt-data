#State of the program right berfore the function call: **
def func():
    n = input()
    while n:
        n -= 1
        
        for j in range(n):
            print(bin(j + 1)[::-1].find('1') + 1)
        
    #State of the program after the loop has been executed: `n` is 0, `output` is 0, `j` is -1
#Overall this is what the function does:The function reads an input from the user and decrements it until reaching 0. For each value of `n`, it iterates over the range from 0 to `n-1`, prints the position of the rightmost '1' bit in the binary representation of each number, and then discards the result. The function does not accept any parameters and does not return any value.

