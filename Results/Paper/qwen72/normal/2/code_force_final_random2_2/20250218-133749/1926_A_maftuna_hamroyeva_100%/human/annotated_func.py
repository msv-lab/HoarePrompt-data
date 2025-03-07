#State of the program right berfore the function call: t is an integer such that 1 <= t <= 32, representing the number of test cases. Each test case contains a string of length 5, consisting only of the characters 'A' and 'B'. All t strings are distinct.
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
        
    #State: `t` is an integer such that 1 <= t <= 32, `i` is `t-1`, `a` is the last user-provided string, `l` is the number of 'A' characters in the last string `a`, and `h` is the number of non-'A' characters in the last string `a`. If `l` > `h`, the number of 'A' characters (`l`) is greater than the number of non-'A' characters (`h`). Otherwise, `l` is less than or equal to `h`.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, where `1 <= t <= 32`, indicating the number of test cases. For each test case, it reads a string of length 5 consisting only of the characters 'A' and 'B'. It then counts the number of 'A' and 'B' characters in the string. If the number of 'A' characters is greater than the number of 'B' characters, it prints 'A'; otherwise, it prints 'B'. After processing all `t` test cases, the function completes, and the final state is that `t` lines have been printed, each containing either 'A' or 'B' based on the comparison of 'A' and 'B' counts in the corresponding input string.

