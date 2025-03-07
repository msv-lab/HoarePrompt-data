#State of the program right berfore the function call: The function is expected to handle multiple test cases, where the number of test cases t is an integer such that 1 ≤ t ≤ 32. Each test case consists of a string of length 5 containing only the characters 'A' and 'B'. All strings across the test cases are distinct.
def func():
    t = int(input())
    for q in range(t):
        ac = 0
        
        bc = 0
        
        s = input()
        
        for i in s:
            if i == 'A':
                ac += 1
            else:
                bc += 1
        
        if ac > bc:
            print('A')
        else:
            print('B')
        
    #State: `t` is an integer input by the user where 1 ≤ t ≤ 32, `q` is `t-1`, `s` is the last string input by the user, `ac` is the number of 'A' characters in `s`, and `bc` is the number of non-'A' characters in `s`. For each test case, if the number of 'A' characters (`ac`) is greater than the number of non-'A' characters (`bc`), the program prints 'A'. Otherwise, it prints 'B'.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases (1 ≤ t ≤ 32). For each test case, it reads a string `s` of length 5 containing only 'A' and 'B'. It counts the occurrences of 'A' and 'B' in `s`. If the count of 'A' is greater than the count of 'B', it prints 'A'; otherwise, it prints 'B'. After processing all test cases, the function completes its execution.

