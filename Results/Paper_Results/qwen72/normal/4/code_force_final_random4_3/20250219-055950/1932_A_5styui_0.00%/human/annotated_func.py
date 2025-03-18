#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 1000) representing the number of test cases, and a list of tuples, where each tuple contains an integer n (1 ≤ n ≤ 50) and a string of n characters. The string consists of '.', '@', and '*' characters, representing empty cells, cells with coins, and cells with thorns, respectively. It is guaranteed that the first cell of each path is empty.
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
        
    #State: `s` is 0, `t` is an input integer (1 ≤ t ≤ 1000), `a` is 0, `i` is `a - 1` (which is -1 after the loop completes), `d` is the last input integer, `b` is the last input string, and `j` is the last index of `b` (i.e., `len(b) - 1`).
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads an integer `n` and a string `b` of length `n` from the input. The string `b` consists of '.', '@', and '*' characters, representing empty cells, cells with coins, and cells with thorns, respectively. The function counts the number of '@' characters (coins) in the string `b` until it encounters a '*' character (thorn), at which point it stops counting and prints the total count of coins for that test case. After processing all test cases, the function does not return any value, but the final state of the program is such that `s` is 0, `a` is the number of test cases, `i` is `a - 1` (which is `t - 1`), `d` is the last input integer, `b` is the last input string, and `j` is the last index of `b` (i.e., `len(b) - 1`).

