#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 10, and s is a string of length n consisting of characters 'W' and 'B', where at least one character in s is 'B'.
def func():
    n = int(input())
    for i in range(n):
        t = int(input())
        
        x = list(input())
        
        if 'B' in x:
            start = x.index('B')
            end = len(x) - x[::-1].index('B') - 1
            print(end - start)
        else:
            print(0)
        
    #State: Postcondition: `n` is an input integer, `i` is equal to `n`, `x` is a list of characters from the final input string. If 'B' is found in the list `x`, `start` is the index of the first 'B' and `end` is the index of the last 'B' in the reversed list `x`. If 'B' is not found in the list `x`, no additional variables are modified.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `n` and then reads a string `s` of length `n` consisting of characters 'W' and 'B'. It finds the positions of the first and last 'B' characters in the string `s` and prints the distance between these two positions. If the string `s` does not contain any 'B' characters, it prints 0.

