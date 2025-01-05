#State of the program right berfore the function call: N is an integer between 2 and 500 (inclusive).**
def func():
    n = input()
    while n:
        n -= 1
        
        for j in range(n):
            print(bin(j + 1)[::-1].find('1') + 1)
        
    #State of the program after the loop has been executed: `N` is an integer between 2 and 500, `n` is 0
#Overall this is what the function does:The function `func` reads input from the user and decrements the input value until it reaches 0. Then, it iterates over a range based on the decremented input value and prints the position of the first '1' in the reversed binary representation of the numbers in the range. The function does not accept any input parameters and does not have any return value.

