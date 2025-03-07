#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 50, and the second line of input is a string of n characters consisting only of '.', '@', and '*', where the first character is always '.', indicating that the path starts with an empty cell.
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
                thorn == 0
        
        print(ret)
        
    #State: All characters in the list `s` have been processed, `ret` is the total count of '@' characters in `s`, and `thorn` is 0.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer n and a string of length n containing '.', '@', and '*'. It counts the number of '@' characters in each string, breaking early if two '*' characters are encountered consecutively. After processing all test cases, it prints the count of '@' characters for each case.

