#State of the program right berfore the function call: t is an integer such that 1 <= t <= 32, and for each of the t test cases, there is a string of length 5 consisting of the characters 'A' and 'B'. All t strings are distinct.
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
        
    #State: `t` is an input integer between 1 and 32; `q` is equal to `t` after the loop completes; for each of the `t` test cases, `ac` and `bc` represent the counts of 'A' and 'B' (or non-'A') characters, respectively, in each string `s` provided by the user.
    if (ac > bc) :
        print('A')
        #This is printed: A
    else :
        print('B')
        #This is printed: B
    #State: `t` is an input integer between 1 and 32; `q` is equal to `t` after the loop completes; for each of the `t` test cases, `ac` and `bc` represent the counts of 'A' and 'B' (or non-'A') characters, respectively, in each string `s` provided by the user. In the current test case, if `ac` is greater than `bc`, then `ac` is greater than `bc`; otherwise, `ac` is less than or equal to `bc`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, where each test case consists of a distinct string of length 5 containing only 'A' and 'B'. For each test case, it counts the occurrences of 'A' and 'B' and prints 'A' if 'A' appears more times, otherwise it prints 'B'.

