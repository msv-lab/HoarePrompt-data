#State of the program right berfore the function call: t is an integer such that 1 <= t <= 32, and for each of the t test cases, there is a string of length 5 consisting only of the characters 'A' and 'B'. All t strings are distinct.
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
        
    #State: `t` is greater than 0, `q` is `t-1`, `s` is the last input string, `ac` is the count of 'A' characters in the last string `s`, and `bc` is the count of non-'A' characters in the last string `s`. If `ac` is greater than `bc`, the last printed character is 'A'. Otherwise, the last printed character is 'B'.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, where each test case is a string of length 5 consisting only of the characters 'A' and 'B'. For each test case, it prints 'A' if the count of 'A' characters in the string is greater than the count of 'B' characters; otherwise, it prints 'B'.

