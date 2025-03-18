#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 50, and the second line of input is a string of n characters consisting only of '.', '@', and '*', where '.' represents an empty cell, '@' represents a cell with a coin, and '*' represents a cell with thorns. Additionally, the first cell is guaranteed to be empty ('.')
def func():
    a = int(input())
    s = 0
    for i in range(a):
        d = int(input())
        
        b = input()
        
        for j in range(len(b)):
            if b[j] == '@':
                s = s + 1
            elif b[j] == '*':
                if j == len(b) - 1:
                    break
                elif b[j + 1] == '*':
                    break
        
        print(s)
        
        s = 0
        
    #State: Output State: `s` is 0, `j` is equal to the length of the string `b`, `i` is 999 (since `a` is the upper limit of the range in the loop, and the loop runs from 0 to `a-1`), `d` is an input integer for each iteration, and `t` remains unchanged as it was not affected by the loop.
    #
    #This means after the loop has executed all its iterations, the variable `s` will be reset to 0 at the end of the last iteration, `j` will be equal to the length of the string `b` (as it is checked at the end of the inner loop), `i` will be 999 (the last value it takes before the loop ends), `d` will hold the last input integer received during the loop, and `t` will remain unchanged because it was not involved in any operations within the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a string of `n` characters ('.', '@', '*'). For each test case, it counts the number of coins ('@') in the string and prints the count. After processing all test cases, it resets the count to zero and continues to the next test case until all `t` test cases are processed. The function does not return any value but prints the count of coins for each test case.

