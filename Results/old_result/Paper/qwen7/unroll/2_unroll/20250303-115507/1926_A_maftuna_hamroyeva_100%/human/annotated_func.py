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
        
    #State: Output State: The value of `t` is an integer between 1 and 32 inclusive. For each of the `t` inputs, if the count of 'A' characters is greater than the count of non-'A' characters in the input string, 'A' is printed; otherwise, 'B' is printed. All other variables remain unchanged.
#Overall this is what the function does:The function processes an integer `t` (1 ≤ t ≤ 32) representing the number of test cases. For each test case, it reads a string of length 5 consisting of 'A' and 'B'. It counts the occurrences of 'A' and 'B' in each string. If the count of 'A' is greater than the count of 'B', it prints 'A'; otherwise, it prints 'B'. After processing all test cases, the function does not return any value.

