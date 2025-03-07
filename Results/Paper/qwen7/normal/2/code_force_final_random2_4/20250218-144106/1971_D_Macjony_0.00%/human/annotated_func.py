#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, s is a binary string with a length between 1 and 500.
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
        
    #State: t is an integer greater than 2 and between 1 and 500, i is t, s is a string with more than one character, count is 4, flag is True, and j is the length of the string s.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t` and a binary string `s`. For each test case, it counts consecutive segments of alternating '0's and '1's in the string `s`, excluding the last segment if it ends with '1'. If any such segment is found, it decrements the count by one. The function prints the final count for each test case.

