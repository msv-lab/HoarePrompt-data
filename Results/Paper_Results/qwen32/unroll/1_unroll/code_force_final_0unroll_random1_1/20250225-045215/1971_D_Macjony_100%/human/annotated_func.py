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
        
        if flag:
            count -= 1
        
        print(count)
        
    #State: For each test case, the output is the count of segments of consecutive identical characters in the string `s`, minus one if there is at least one transition from '0' to '1'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a binary string. For each string, it calculates the number of segments of consecutive identical characters and subtracts one if there is at least one transition from '0' to '1'. The result for each test case is printed.

