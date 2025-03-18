#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 500) representing the number of test cases. For each test case, there is a single binary string s (1 ≤ |s| ≤ 500) consisting of characters '0' and '1'.
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
        
    #State: For each of the `t` test cases, the number of segments of consecutive identical characters in the binary string `s`, minus one if there is at least one '0' followed by a '1', is printed.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, followed by `t` binary strings. For each binary string, it calculates the number of segments of consecutive identical characters and subtracts one if there is at least one occurrence of '0' followed by '1'. It then prints the result for each test case.

