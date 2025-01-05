#State of the program right berfore the function call: N is an integer between 2 and 500 (inclusive).**
def func():
    n = input()
    while n:
        n -= 1
        
        for j in range(n):
            print(bin(j + 1)[::-1].find('1') + 1)
        
    #State of the program after the loop has been executed: N is between 2 and 500, n is 0, j is 0
#Overall this is what the function does:The function prompts the user to input a value for n. It then iterates n times, decrementing the value of n each time. Within each iteration, it iterates over a range of numbers, converts each number to binary, finds the position of the rightmost '1' bit, and prints that position. The function does not accept any parameters and does not return any value.

