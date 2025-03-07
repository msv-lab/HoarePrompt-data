#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 50, and the second line of input is a string of length n consisting of '.', '@', and '*' where '.' denotes an empty cell, '@' denotes a cell with a coin, and '*' denotes a cell with thorns. Additionally, the first cell is guaranteed to be empty ('.')
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
        
    #State: Output State: `t` is a positive integer such that 1 ≤ t ≤ 1000, `a` is an input integer, `s` is 0.
    #
    #Explanation: The loop processes each character of the string `b` for each iteration of the outer loop (controlled by `i`). If a character `@` is found, `s` is incremented. If a character `*` is found, the inner loop breaks without further processing. After processing each string `b`, `s` is printed and reset to 0 for the next iteration. Since `s` is reset to 0 at the end of each iteration of the outer loop, the final value of `s` will always be 0 regardless of the input strings `b`.
#Overall this is what the function does:The function processes input data for up to 1000 test cases. For each test case, it reads an integer n and a string of length n consisting of '.', '@', and '*', then counts the number of cells with coins ('@'). The function prints the count for each test case and resets the count to 0 after processing each string. The final output consists of the count of cells with coins for each test case.

