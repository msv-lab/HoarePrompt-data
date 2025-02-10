#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 50, and the second line of input is a string of n characters consisting only of '.', '@', and '*', where the first character is always '.', indicating that the path starts with an empty cell.
def func():
    for _ in range(int(input())):
        len = int(input())
        
        s = list(input())
        
        ret = 0
        
        thorn = 0
        
        for i in s:
            if i == '@':
                thorn = 0
                ret += 1
            elif i == '*':
                thorn += 1
                if thorn == 2:
                    break
            else:
                thorn = 0
        
        print(ret)
        
    #State: Output State: After the loop executes all its iterations, `t` remains an integer such that \(1 \leq t \leq 1000\), `len` contains the total number of characters in the input string for the last test case, `s` is a list of characters from the last input string, `ret` is the count of paths that were not terminated by two consecutive '*', which can be 0, 1, or any value up to the number of '@' characters in the string, and `thorn` is 2 if any character in `s` is '*', otherwise `thorn` is 0. The variable `i` holds the last character processed in the list `s`.
    #
    #This means that `ret` will be incremented every time an '@' is encountered, and the loop will terminate early if two consecutive '*' are found. The final value of `ret` will reflect the number of valid paths through the string, and `thorn` will indicate whether any '*' characters were processed.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n` and a string of length `n` consisting of '.', '@', and '*'. It counts the number of valid paths through each string, where a valid path is defined as a sequence that does not contain two consecutive '*'. If two consecutive '*' are found, the counting stops for that particular string. The function outputs the count of valid paths for each string and does not return any value explicitly.

