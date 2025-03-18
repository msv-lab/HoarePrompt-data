#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 1000) representing the number of test cases, and a list of strings paths where each string s in paths has a length n (1 ≤ n ≤ 50) and consists of characters '.', '@', and '*' representing empty cells, cells with coins, and cells with thorns, respectively. The first cell of each string is guaranteed to be empty.
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
        
    #State: `a` is an input integer, `t` is an integer (1 ≤ t ≤ 1000), `paths` is a list of strings where each string `s` has a length `n` (1 ≤ n ≤ 50) and consists of characters '.', '@', and '*', and the first cell of each string is guaranteed to be empty; `s` is 0.
#Overall this is what the function does:The function `func` reads an integer `a` from the input, which represents the number of test cases. For each test case, it reads an integer `d` (which is not used in the function) and a string `b` representing a path. The function counts the number of '@' characters in the string `b` and stops counting if it encounters a '*' character. After processing each test case, it prints the count of '@' characters and resets the count to 0. The function does not return any value. After the function concludes, the input integer `a` and the list of strings `b` (one for each test case) are consumed, and the final state of the program is that the counts of '@' characters for each test case have been printed.

