#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, s is a string consisting of characters '0' and '1' with length 1 ≤ |s| ≤ 500.
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
        
    #State: 
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, followed by `t` strings `s` each consisting of characters '0' and '1'. For each string `s`, it calculates and prints the number of segments formed by consecutive identical characters, reducing the count by one if there is at least one transition from '0' to '1'.

