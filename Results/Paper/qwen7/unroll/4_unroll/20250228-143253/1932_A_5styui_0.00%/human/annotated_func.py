#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000. For each test case, n is a positive integer such that 1 ≤ n ≤ 50, and the second line of input is a string of length n consisting of '.', '@', and '*' where '.' represents an empty cell, '@' represents a cell with a coin, and '*' represents a cell with thorns. Additionally, the first cell is guaranteed to be empty ('.').
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
        
    #State: Output State: `t` is a positive integer such that 1 ≤ t ≤ 1000, `a` is an input integer between 1 and 50 (inclusive), `s` is 0.
    #
    #Explanation: The loop processes `a` inputs from the user, each followed by a string input. For each string, it counts the number of '@' characters and then prints the count. After printing, it resets `s` to 0. Since `s` is reset to 0 at the end of each iteration, the final value of `s` will always be 0 regardless of the inputs provided. Therefore, the value of `s` remains unchanged at 0 after all iterations of the loop.
#Overall this is what the function does:The function processes input data for up to 1000 test cases. For each test case, it reads an integer \( n \) and a string representing a row of cells. The string consists of '.', '@', and '*' characters, where '.' represents an empty cell, '@' represents a cell with a coin, and '*' represents a cell with thorns. The function counts the number of cells with coins ('@') in each row and prints the count. After processing each row, it resets the count to zero. The function does not return any value but prints the count of coins for each test case.

