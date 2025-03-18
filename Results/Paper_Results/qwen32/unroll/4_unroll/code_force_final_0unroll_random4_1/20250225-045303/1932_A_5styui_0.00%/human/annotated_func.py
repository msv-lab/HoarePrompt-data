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
        
    #State: t is an integer such that 1 <= t <= 1000; n is an integer such that 1 <= n <= 50; path is a string of length n consisting of characters '.', '@', and '*', where the first character is guaranteed to be '.'; a is an input integer; s is 0.
#Overall this is what the function does:The function reads an integer `a` representing the number of test cases. For each test case, it reads another integer `d` (which is not used) and a string `b` of length `n` consisting of '.', '@', and '*'. It counts the number of '@' characters in the string `b` until it encounters a '*' character, then prints this count and resets the count for the next test case.

