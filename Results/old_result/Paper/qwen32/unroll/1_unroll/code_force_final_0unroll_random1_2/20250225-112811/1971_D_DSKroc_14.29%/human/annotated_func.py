#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, s is a binary string (a string consisting of characters '0' and '1') such that 1 ≤ |s| ≤ 500.
def func():
    t = int(input())
    for q in range(t):
        s = input()
        
        count = 0
        
        for i in range(len(s) - 1):
            if int(s[i]) > int(s[i + 1]):
                count += 1
        
        print(count + 1)
        
    #State: a series of integers, each representing the number of segments in the respective binary string for each test case.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads a binary string `s`. It then calculates and prints the number of segments in the binary string, where a segment is defined as a contiguous substring of '1's.

