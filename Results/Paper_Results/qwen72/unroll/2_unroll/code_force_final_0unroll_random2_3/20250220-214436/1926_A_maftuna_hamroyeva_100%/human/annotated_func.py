#State of the program right berfore the function call: The function `func` is expected to be called within a loop or context where it processes multiple test cases. Each test case involves a string of length 5 consisting of the letters 'A' and 'B'. The number of test cases, `t`, is an integer such that 1 <= t <= 32, and all strings in the test cases are distinct.
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
        
    #State: The loop has processed all `t` test cases, and for each test case, it has printed 'A' if the number of 'A's in the string is greater than the number of 'B's, and 'B' otherwise. The variables `l` and `h` are reset to 0 for each test case, so they do not retain any values from one iteration to the next.
#Overall this is what the function does:The function `func` processes a series of test cases, where each test case is a distinct string of length 5 consisting of the letters 'A' and 'B'. The number of test cases, `t`, is an integer between 1 and 32. For each test case, the function counts the number of 'A's and 'B's in the string. If the number of 'A's is greater than the number of 'B's, it prints 'A'; otherwise, it prints 'B'. After processing all test cases, the function has printed a result ('A' or 'B') for each one, and the variables `l` and `h` are reset to 0 for each test case.

