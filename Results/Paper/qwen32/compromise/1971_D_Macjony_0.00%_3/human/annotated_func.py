#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each of the t test cases, s is a string consisting of characters '0' and '1' with length 1 ≤ |s| ≤ 500.
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
            j += 1
        
        if flag:
            count -= 1
        
        print(count)
        
    #State: The output state consists of `t` integers, each representing the adjusted number of segments of identical characters in each respective input string `s`, considering the special case where a '0' is followed by a '1'.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads a binary string `s` and calculates the number of segments of identical characters in the string, adjusting the count by subtracting one if there is at least one occurrence of '0' immediately followed by '1'. It then prints the adjusted count for each test case.

