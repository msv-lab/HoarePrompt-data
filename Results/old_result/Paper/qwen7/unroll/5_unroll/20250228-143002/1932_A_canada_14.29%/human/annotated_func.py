#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 50, and the second line of input is a string of n characters where each character is either '.', '@', or '*'. The first character of the string is always '.', indicating that the starting cell is empty.
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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 50, and the second line of input is a string of n characters where each character is either '.', '@', or '*'. The first character of the string is always '.', indicating that the starting cell is empty. After executing the loop, `ret` is an integer representing the number of times the loop encountered the character '@' before encountering two consecutive '*' characters, and if two consecutive '*' characters were encountered, the loop breaks early.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and a string of length \( n \) made up of '.', '@', or '*'. It counts the number of times the character '@' appears before encountering two consecutive '*' characters in each string. If two consecutive '*' characters are found, the counting stops early. The function outputs the count for each test case.

