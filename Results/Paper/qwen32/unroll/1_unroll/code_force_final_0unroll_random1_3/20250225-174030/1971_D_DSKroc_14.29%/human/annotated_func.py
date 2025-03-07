#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 500) representing the number of test cases. Each of the following t lines contains a single string s (1 ≤ |s| ≤ 500) consisting of characters '0' and '1'.
def func():
    t = int(input())
    for q in range(t):
        s = input()
        
        count = 0
        
        for i in range(len(s) - 1):
            if int(s[i]) > int(s[i + 1]):
                count += 1
        
        print(count + 1)
        
    #State: For each test case, the number of segments the string `s` can be divided into such that each segment is non-decreasing is printed. The variable `t` remains unchanged, and `s` is the last input string processed.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads a string `s` consisting of '0's and '1's. It then calculates and prints the number of segments the string can be divided into such that each segment is non-decreasing.

