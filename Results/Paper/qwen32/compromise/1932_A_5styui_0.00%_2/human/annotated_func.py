#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 1 <= n <= 50, and the path is a string of length n consisting of characters '.', '@', and '*', where the first character is guaranteed to be '.'.
def func():
    a = int(input())
    s = 0
    for i in range(a):
        d = int(input())
        
        b = input()
        
        for j in range(len(b)):
            if b[j] == '@':
                s = s + 1
            elif b[j] == '*':
                if b[:]:
                    break
                elif b[j + 1] == '*':
                    break
        
        print(s)
        
        s = 0
        
    #State: `t` is an integer such that 1 <= t <= 1000; `n` is an integer such that 1 <= n <= 50; `path` is a string of length `n` consisting of characters '.', '@', and '*', where the first character is guaranteed to be '.'; `a` is greater than 0; `i` is `a-1`; `d` is an input integer from the last iteration; `b` is a non-empty string from the last iteration; `j` is the length of `b` if the loop completes all iterations without encountering '*', or the index where the loop breaks due to '*'; `s` is 0.
#Overall this is what the function does:The function reads an integer `a` representing the number of test cases. For each test case, it reads another integer `d` and a string `b` of length `d` consisting of '.', '@', and '*'. It counts the number of '@' characters in the string `b` until it encounters a '*', at which point it stops counting for that test case. It then prints the count for each test case and resets the count for the next test case.

