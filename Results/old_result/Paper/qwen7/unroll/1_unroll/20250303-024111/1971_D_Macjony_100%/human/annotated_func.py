#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, s is a binary string with 1 ≤ |s| ≤ 500.
def func():
    t = int(input())
    for i in range(t):
        s = input()
        
        count = 1
        
        flag = False
        
        j = 0
        
        while j < len(s) - 1:
            if s[j] != s[j + 1]:
                count += 1
                if s[j] == '0' and s[j + 1] == '1':
                    flag = True
            j += 1
        
        if flag:
            count -= 1
        
        print(count)
        
    #State: Output State: t is the number of strings processed, and for each string, count is the length of the longest alternating subsequence minus one if there was a transition from '0' to '1' at any point in the string.
#Overall this is what the function does:The function processes a series of binary strings (up to 500 in number) and calculates the length of the longest alternating subsequence for each string. If there is a transition from '0' to '1' anywhere in the string, it subtracts one from the count. The function outputs the count for each string and the total number of strings processed.

