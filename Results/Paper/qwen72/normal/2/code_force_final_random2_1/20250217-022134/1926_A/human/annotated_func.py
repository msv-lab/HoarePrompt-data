#State of the program right berfore the function call: t is an integer such that 1 <= t <= 32, and each of the t test cases contains a string of length 5 consisting of letters 'A' and 'B'. All t strings are distinct.
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
        
    #State: `t` is an input integer between 1 and 32, `i` is `t-1`, `a` is a new input string with 5 characters, `l` is the number of 'A's in `a`, and `h` is the number of 'B's in `a`. If the number of 'A's in `a` is greater than the number of 'B's in `a`, then `l` > `h`. Otherwise, the number of 'A's in `a` is less than or equal to the number of 'B's in `a`, so `l` ≤ `h`. Each of the `t` test cases contains a string of length 5 consisting of letters 'A' and 'B', all `t` strings are distinct.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases, where `1 <= t <= 32`. For each of the `t` test cases, it reads a string of length 5 consisting of letters 'A' and 'B'. The function counts the occurrences of 'A' and 'B' in each string. If the number of 'A's is greater than the number of 'B's, it prints 'A'; otherwise, it prints 'B'. After processing all `t` test cases, the function has printed a result ('A' or 'B') for each test case. The final state of the program is that `t` results have been printed, one for each test case.

