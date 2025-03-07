#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each of the t test cases, there is a string s consisting of characters '0' and '1' such that 1 ≤ |s| ≤ 500.
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
        
    #State: `i` is `t`, `s` is the last input string, `j` is `len(s) - 1`, `count` is the final count for the last test case, `flag` is `True` if there was a '01' transition in the last test case, otherwise `False`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads a string `s` consisting of characters '0' and '1'. It then calculates and prints the number of segments in the string `s` where consecutive characters are different, reducing the count by one if there is at least one '01' transition in the string.

