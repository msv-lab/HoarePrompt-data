#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 50, and the second line of input is a string of length n consisting of '.', '@', and '*', where '.' represents an empty cell, '@' represents a cell with a coin, and '*' represents a cell with thorns. Additionally, the first cell is guaranteed to be empty ('.')
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
                if b[:]:
                    break
                elif b[j + 1] == '*':
                    break
        
        print(s)
        
        s = 0
        
    #State: Output State: After the loop executes all its iterations, `s` will be the total count of '@' characters across all strings `b` provided during the loop's execution, `i` will be the sum of the lengths of all strings `b`, `d` will retain the value it had before the loop started (as it is not used within the loop), `a` will remain unchanged, and `j` will be the length of the last string `b` processed. The loop will break if it encounters two consecutive '*' characters in any string `b`.
    #
    #This means that `s` accumulates the count of '@' symbols from all inputs, while `i` keeps track of the cumulative length of all strings `b`. The variables `d` and `a` remain unchanged throughout the loop's execution.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and a string of length \( n \) containing '.', '@', and '*'. It counts the number of '@' characters in each string and prints this count for each test case. If the function encounters two consecutive '*' characters in any string, it breaks out of the loop for that string. The function does not return any value but prints the count of '@' characters for each test case.

