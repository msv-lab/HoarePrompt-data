#State of the program right berfore the function call: N is an integer between 2 and 500 (inclusive).**
def func():
    n = input()
    while n:
        n -= 1
        
        for j in range(n):
            print(bin(j + 1)[::-1].find('1') + 1)
        
    #State of the program after the loop has been executed: N is an integer between 2 and 500, `n` is 1, `j` is 0
#Overall this is what the function does:The function prompts the user for input, decrements the input by 1 in a loop, and then iterates over a range based on the decremented input. During each iteration, it prints the position of the rightmost set bit in the binary representation of the current number. The function does not accept any parameters and operates within the range of integers from 2 to 500 (inclusive).

