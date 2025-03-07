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
        
    #State: `t` is an integer between 1 and 32, inclusive; `ac` is the count of 'A's in the last string `s`; `bc` is the count of non-'A' characters in the last string `s`; `s` is the last string provided by the user input; `q` is equal to `t`.
    if (ac > bc) :
        print('A')
        #This is printed: A
    else :
        print('B')
        #This is printed: B
    #State: `t` is an integer between 1 and 32, inclusive; `q` is equal to `t`; `s` is the last string provided by the user input; `ac` is the count of 'A's in `s`; `bc` is the count of non-'A' characters in `s`. If `ac` is greater than `bc`, then `ac` is greater than `bc`; otherwise, `ac` is less than or equal to `bc`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, where each test case consists of a distinct string of length 5 containing only the characters 'A' and 'B'. For each string, it counts the occurrences of 'A' and 'B'. After processing all test cases, it prints 'A' if the count of 'A's in the last string is greater than the count of 'B's; otherwise, it prints 'B'.

