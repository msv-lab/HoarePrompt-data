#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, and for each of the t test cases, s is a string consisting of characters '0' and '1' with length 1 <= |s| <= 500.
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
        
    #State: A series of integers, each representing the adjusted count of transitions for each test case.
#Overall this is what the function does:The function accepts an integer `t` representing the number of test cases. For each test case, it processes a string `s` consisting of '0's and '1's. It then calculates and prints the number of transitions between '0' and '1' in the string, subtracting one if there is at least one '01' transition.

