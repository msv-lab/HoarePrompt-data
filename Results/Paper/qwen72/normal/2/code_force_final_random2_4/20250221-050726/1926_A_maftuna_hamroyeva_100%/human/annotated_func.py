#State of the program right berfore the function call: t is an integer such that 1 <= t <= 32, representing the number of test cases. Each test case contains a string of length 5 consisting of letters 'A' and 'B', and all t strings are distinct.
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
        
    #State: `t` is an integer such that 1 <= t <= 32, `i` is `t-1`, `a` is the last input string, `l` is the number of 'A' characters in the last input string `a`, and `h` is the number of non-'A' characters in the last input string `a`. If the number of 'A' characters (`l`) is greater than the number of non-'A' characters (`h`), then `l` > `h`. Otherwise, `l` <= `h`.
#Overall this is what the function does:The function `func` reads an integer `t` (1 ≤ t ≤ 32) indicating the number of test cases. For each test case, it reads a string of length 5 consisting of 'A' and 'B'. It counts the occurrences of 'A' and 'B' in each string and prints 'A' if the count of 'A' is greater than the count of 'B', otherwise it prints 'B'. After processing all test cases, the function terminates without returning any value. The final state of the program is that `t` test cases have been processed, and for each test case, either 'A' or 'B' has been printed based on the comparison of counts.

