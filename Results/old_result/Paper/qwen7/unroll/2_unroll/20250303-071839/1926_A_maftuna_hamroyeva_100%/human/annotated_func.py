#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 32, and for each test case, the input string is a string of length 5 consisting of the letters 'A' and 'B'. All t strings across all test cases are distinct.
def func():
    t = int(input())
    for i in range(t):
        a = input()
        
        l = 0
        
        h = 0
        
        for j in a:
            if j == 'A':
                l += 1
            else:
                h += 1
        
        if l > h:
            print('A')
        else:
            print('B')
        
    #State: Output State: The value of `t` remains unchanged, and for each string `a` entered according to the number specified by `t`, the output is either 'A' or 'B' based on whether the count of 'A' characters is greater than the count of non-'A' characters in each string `a`.
#Overall this is what the function does:The function processes `t` test cases, where `t` is an integer between 1 and 32. For each test case, it reads a string of length 5 consisting of 'A' and 'B'. It then counts the occurrences of 'A' and 'B' in each string. Based on whether the count of 'A' is greater than the count of 'B', it prints either 'A' or 'B'. The function does not return any value; it only prints the results for each test case.

