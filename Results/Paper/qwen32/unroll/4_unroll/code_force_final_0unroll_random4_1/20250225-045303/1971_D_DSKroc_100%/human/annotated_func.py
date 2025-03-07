#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 500) representing the number of test cases. For each test case, there is a single binary string s (1 ≤ |s| ≤ 500) consisting of characters '0' and '1'.
def func():
    t = int(input())
    for q in range(t):
        s = input()
        
        count = 0
        
        flag = 0
        
        for i in range(len(s) - 1):
            if int(s[i]) != int(s[i + 1]):
                count += 1
            if int(s[i]) < int(s[i + 1]):
                flag = 1
        
        if flag == 0:
            print(count + 1)
        else:
            print(count)
        
    #State: a series of numbers, each representing the result of processing one test case.
#Overall this is what the function does:The function processes a series of binary strings, each representing a test case, and outputs the number of transitions between '0' and '1' in each string. If the string is non-decreasing (i.e., it does not have a '0' followed by a '1'), it adds one to the count of transitions before outputting the result.

